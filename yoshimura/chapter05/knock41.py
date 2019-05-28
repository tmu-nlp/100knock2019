'''
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
'''
from knock40 import Morph


class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self):
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return(f'surface: {surface}\tdst: {self.dst}\tsrcs: {self.srcs}')

    def normalized_surface(self):
        '''句読点などの記号を除いた表層を返す'''
        n_surface = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                n_surface += morph.surface
        return n_surface

    def surface(self):
        '''表層を返す'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return surface

    def check_pos(self, pos):
        '''引数の品詞が含まれているたらTrueを返す'''
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def get_surfaces(self, feature, s):
        '''featureがsの表層形を全て返す'''
        if feature == 'pos':
            return [morph.base for morph in self.morphs if morph.pos == s]
        if feature == 'pos1':
            return [morph.base for morph in self.morphs if morph.pos1 == s]
        # return ''

    def get_sahen_wo(self):
        '''「サ変接続名詞+を（助詞）」で構成される文節があればそれを返す'''
        for i in range(len(self.morphs) - 1):
            if self.morphs[i].pos1 == 'サ変接続' and self.morphs[i + 1].surface == 'を':
                return self.morphs[i].surface + self.morphs[i + 1].surface
        return ''


def get_chunk_list(file_path: str):
    with open(file_path) as f:
        chunks = {}  # Chunkオブジェクトのidx : Chunkオブジェクト
        for line in f:
            line = line.rstrip()

            # 係り受け情報の場合
            if line[0] == '*':
                idx = int(line.split(' ')[1])  # 文節番号
                dst = int(line.split(' ')[2][:-1])  # 係り先の文節番号（係り先なし:-1)

                # Chunkオブジェクトをchunksに追加
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                # 係り先があって係り先のオブジェクトが存在しなければ作成してそのsrcsに文節番号を追加
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            # 形態素情報の場合
            elif line != 'EOS' and line[:1] != '*':
                line = ','.join(line.split("\t")).split(',')

                # Morphクラスをリストに追加
                chunks[idx].morphs.append(Morph(
                    line[0],  # surface
                    line[7],  # base
                    line[1],  # pos
                    line[2]   # pos1
                ))

            # 文の終わりの場合
            elif line == 'EOS':
                if len(chunks) != 0:
                    yield [chunks[i] for i in sorted(chunks.keys())]
                else:
                    yield []
                chunks = {}


if __name__ == '__main__':
    for i, chunks in enumerate(get_chunk_list("neko.txt.cabocha"), 1):
        if i == 8:
            for chunk in chunks:
                print(chunk)
            break


# フォーマット情報
# https://taku910.github.io/cabocha/ 