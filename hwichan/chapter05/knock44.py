import pydot_ng as pydot


class Morph:
    # コンストラクタ
    # surface(表層形), base(基本形), pos(品詞), pos1(品詞細分類1)
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    # __str__ オブジェクトを文字列にして返す
    def __str__(self):
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self):
        self.morphs = []  # 文節のmorph、1文節ごとのMorphインスタンスが格納
        self.srcs = []  # 係り元文節番号、二個ある場合があるから配列
        self.dst = -1  # 係り先文節番号

    def __str__(self):
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

    def return_surface(self):
        surface = ''
        for morph in self.morphs:
            if morph.pos != '記号':  # 句読点は出力しない
                surface += morph.surface
        return surface


def make_list(filename: str):
    with open(filename, 'r') as f:
        chunks = dict()  # idxをkeyにして,keyごとにChunkインスタンスを格納
        idx = -1  # 文節番号
        for line in f:
            if line == 'EOS\n':  # 1文の終了, chunksをyieldで返す
                if len(chunks) > 0:  # EOS\tが連続するとこがあるから

                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])  # key(文節番号)でソート
                    yield list(zip(*sorted_tuple))[1]  # value('{}\tsrcs{}\tdst[{}]')のみ返す
                    chunks.clear()

                else:
                    yield []

            elif line[0] == '*':  # 最初の文字が'*'の場合、係り受け解析結果
                # * 0 2D 0/0 -0.764522
                line = line.split(' ')
                idx = int(line[1])  # 文節番号、0
                # 2D
                dst = int(line[2][:-1])  # 係り先番号、2

                # 下の処理(係り元番号のセット)をするときもChunkインスタンスを生成するためkeyがかぶってないか確認
                if idx not in chunks:  # 文節番号のキーがなかったらChunkを生成
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst  # 係り先番号をセット(dst)

                # 係り元番号のセット(srcs)、係り先番号のChunkに現在の文節番号をsrcsにセット
                if dst != -1:  # dst = -1は係り先がない
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    # 係り先の文節では現在の文節が係り元
                    chunks[dst].srcs.append(idx)

            else:
                # 吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ,,
                line = line.split('\t')
                cal1 = line[0]
                cal2 = line[1].split(',')
                chunks[idx].morphs.append(Morph(cal1, cal2[6], cal2[0], cal2[1]))


def make_graph(edges: list):
    graph = pydot.Dot(graph_type='digraph')  # digraph有効グラフの指定

    for edge in edges:
        id1 = edge[0][0]
        label1 = edge[0][1]
        id2 = edge[1][0]
        label2 = edge[1][1]

        # idがないと同じ文節が出たときに混ざってしまう
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # 上で追加したノードをつなぐエッジを追加、idで判断
        graph.add_edge(pydot.Edge(id1, id2))

    return graph


def main():
    # 入力文字によるgraphの作成
    # filename = 'graph.txt'
    # with open(filename, mode='w') as out_file:
    #     out_file.write(input('文字列を入力してください--> '))
    #
    # write_file(read_file(filename), filename)

    for i, chunks in enumerate(make_list('neko.txt.cabocha')):
        if i == 5:
            edges = []
            for j, chunk in enumerate(chunks):  # j : 文節番号
                if chunk.dst != -1:
                    src = chunk.return_surface()
                    dst = chunks[chunk.dst].return_surface()
                    if src != '' and dst != '':
                        edges.append(((j, src), (chunk.dst, dst)))

            if len(edges) > 0:
                graph = make_graph(edges)
                graph.write_png('result.png')

            break


if __name__ == "__main__":
    main()

