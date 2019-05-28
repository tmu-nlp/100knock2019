'''
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
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
        clause = ''.join(m.surface for m in self.morphs if m.pos != '記号')
        return clause

    def has_pos(self, pos):
        for m in self.morphs:
            if m.pos == pos:
                return True
        return False


if __name__ == "__main__":
    res = []
    for chunks in cabocha_into_chunks():
        chunks = tuple(map(Chunk_normalized, chunks.values()))
        for c in chunks:
            if c.dst == -1:
                continue
            if c.has_pos('名詞') and chunks[c.dst].has_pos('動詞'):
                res.append(f'{c.norm}\t{chunks[c.dst].norm}\n')
    sys.stdout.writelines(res)
    message(f'{len(res)} 行書き出しました')
