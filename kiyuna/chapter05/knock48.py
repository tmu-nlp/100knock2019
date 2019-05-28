'''
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．

- 各文節は（表層形の）形態素列で表現する
- パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する

「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．

    吾輩は -> 見た
    ここで -> 始めて -> 人間という -> ものを -> 見た
    人間という -> ものを -> 見た
    ものを -> 見た
'''
import sys
from knock41 import cabocha_into_chunks, Chunk


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


class Chunk_normalized(Chunk):
    def __init__(self, chunk):
        self.morphs, self.dst, self.srcs = (*chunk,)
        self.norm = self.norm()

    def norm(self):
        # 各文節は（表層形の）形態素列で表現する
        clause = ''.join(m.surface for m in self.morphs if m.pos != '記号')
        return clause

    def has_pos(self, pos):
        for m in self.morphs:
            if m.pos == pos:
                return True
        return False

    def get_pos(self, pos):
        res = []
        for m in self.morphs:
            if m.pos == pos:
                res.append(m)
        return res

    def has_sahen_wo(self):
        cond1 = cond2 = False
        for m in self.morphs:
            if m.pos1 == 'サ変接続':
                cond1 = True
            if m.pos == '助詞' and m.base == 'を':
                cond2 = True
        return cond1 and cond2


if __name__ == "__main__":
    res = []
    for chunks in cabocha_into_chunks():
        chunks = tuple(map(Chunk_normalized, chunks.values()))
        for dc in chunks:
            if not dc.has_pos('名詞'):
                continue
            if dc.dst == -1:
                res.append(dc.norm + '\n')
                continue
            tmp = [dc.norm]
            dst = dc.dst
            # パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
            while dst != -1:
                tmp.append(chunks[dst].norm)
                dst = chunks[dst].dst
            res.append(' -> '.join(tmp) + '\n')
    sys.stdout.writelines(res)
    message(f'{len(res)} 行書き出しました')
