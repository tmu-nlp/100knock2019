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

    # 最左の動詞ということは一番初めにヒットした動詞？
    def check_verb(self):
        for morph in self.morphs:
            if morph.pos == "動詞":
                return morph

    # 助詞が複数ある場合は一つのみ選択し格助詞を優先、または最後の助詞を選択
    # くるにも 31456
    # 及ばんさと 31460
    def check_josi(self):
        josi_list = []

        for morph in self.morphs:
            if morph.pos1 == "格助詞":
                return morph
            elif morph.pos == "助詞":
                josi_list.append(morph)

        if josi_list:
            return josi_list[len(josi_list) - 1]

    # 名詞の入った文節を返す
    def check_noun(self):
        for morph in self.morphs:
            if morph.pos == "名詞":
                return self.return_surface()

    # サ変接続名詞＋を（助詞）のものを返す
    def check_sa_wo(self):
        for n, morph in enumerate(self.morphs):
            if morph.pos == "名詞" and morph.pos1 == "サ変接続":  # 品詞が名詞で、詳細がサ変接続
                for morph2 in self.morphs[n+1:]:  # 上でヒットした単語以降の単語（文節の）をループで回し、を（助詞）がつく場合文節のsurfaceを返す
                    if morph2.pos == "助詞" and morph2.surface == "を":
                        return self.return_surface()

    def noun_mask(self, mask):
        result = ''
        for morph in self.morphs:
            if morph.pos == '名詞':
                result += mask
            else:
                result += morph.surface

        return result


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


def main():
    p_list = []  # 最終的にprintするリスト
    for i, chunks in enumerate(make_list('neko.txt.cabocha')):
        if i == 10:
            break
        for j, chunk in enumerate(chunks):
            noun1 = chunk.check_noun()  # 文節が名詞入りかチェック
            dst1 = chunk.dst
            if noun1 and dst1 >= 0:  # 文節が名詞入りで係り先があったら
                for k, next_chunk in enumerate(chunks[j + 1:]):  # noun1以降の文節に対してループ
                    n_list = ''
                    noun2 = next_chunk.check_noun()
                    if noun2:
                        dst2 = next_chunk.dst  # noun2の係り先番号
                        idx = j + k + 1  # noun2の文節番号
                        # noun2の文節番号がdst1(最初の名詞入り文節の係り先)より小さかったら、係り先でぶつかる
                        if idx < dst1:
                            n_list += chunk.noun_mask("x") + ' | ' + next_chunk.noun_mask("y")
                            while True:
                                if dst2 == dst1:
                                    break
                                # dst_chunkはnoun2の係り先文節
                                dst_chunk = chunks[dst2]
                                n_list += ' -> ' + dst_chunk.return_surface()
                                dst2 = dst_chunk.dst  # dst2を次の係り先番号に更新
                            p_list.append(n_list + ' | ' + chunks[dst1].return_surface())
                        # noun2の文節番号がdst1(最初の名詞入り文節の係り先)より大きかったら、nou1の係り先でぶつかる
                        elif idx > dst1 or idx == dst1:
                            n_list += chunk.noun_mask("x")
                            while True:
                                if idx == dst1:
                                    n_list += ' -> ' + chunks[idx].noun_mask('y')
                                    break
                                # nou1の係り先がidxを超えてしまったら
                                elif idx < dst1:
                                    # nou2の文節追加
                                    n_list += ' | ' + chunks[idx].noun_mask('y')
                                    dst2 = chunks[idx].dst
                                    # dst2からdst1までの係り受けパスを追加
                                    while True:
                                        if dst2 == dst1 or dst2 > dst1:
                                            n_list += ' | ' + chunks[dst1].return_surface()
                                            break
                                        n_list += ' -> ' + chunks[dst2].return_surface()
                                        dst2 = chunks[dst2].dst
                                    break
                                dst_chunk = chunks[dst1]
                                dst1 = dst_chunk.dst
                                n_list += ' -> ' + dst_chunk.return_surface()
                            p_list.append(n_list)

    print('\n'.join(p_list))


if __name__ == "__main__":
    main()

