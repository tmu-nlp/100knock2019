'''
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）\
    のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号\
    のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの\
    解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の\
    文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

from knock40 import Morph


class Chunk(Morph):
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def normalized_surface(self):
        """
        記号を除いた表層形を連ねた一文節
        """
        return ''.join(m.surface for m in self.morphs if m.pos != '記号')


def cabocha_Chunk_read() -> []:
    '''
    1文ごとに係り受け解析の結果を返す
    '''
    chunks = []
    dst = 0
    srcs = []
    path = 'neko.txt.cabocha'
    for i, line in enumerate(open(path)):
        # * 1 7D 2/3 -0.506012
        if line.startswith('*'):
            elements = line.split()
            current_no = int(elements[1])
            # print(current_no)
            dst = int(elements[2][:-1])
            # print(dst)
            chunks.append(Chunk([], dst, srcs))
            if dst == -1:
                continue
            while len(srcs) <= dst:
                srcs.append([])
            srcs[dst].append(current_no)
            chunks[current_no].srcs = srcs
            # print(srcs)
        # 書生	名詞,一般,*,*,*,*,書生,ショセイ,ショセイ
        elif '\t' in line:
            surface, elements_str, _ = line.split('\t')
            elements = elements_str.split(',')
            morph = Morph(surface, elements[6], elements[0], elements[1])
            chunks[current_no].morphs.append(morph)
        # EOS
        else:
            if len(chunks) == 0:
                continue
            yield chunks
            chunks = []
            srcs = []


def main():
    for i, chunks in enumerate(cabocha_Chunk_read()):
        if i < 1:
            continue
        for j, chunk in enumerate(chunks):
            print(f'{j}: 係先 {chunk.dst}')
            for morph in chunk.morphs:
                print(f'   {morph.surface} {morph.base} {morph.pos} {morph.pos1}')
        break


if __name__ == "__main__":
    main()
