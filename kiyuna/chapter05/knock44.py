'''
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''
import pydot
from itertools import islice
from knock41 import cabocha_into_chunks, Chunk


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
    def input_k():
        return int(input('Enter a number (0: exit) -> '))

    for k in iter(input_k, 0):
        for chunks in islice(cabocha_into_chunks(), k - 1, k):
            chunks = tuple(map(Chunk_normalized, chunks.values()))
            G = pydot.Dot(graph_type='digraph')
            for i, c in enumerate(chunks):
                if c.norm:
                    color = 'red' if c.has_pos('名詞') else 'black'
                    G.add_node(pydot.Node(i, label=c.norm, color=color))
            for i, c in enumerate(chunks):
                if c.dst == -1:
                    continue
                if c.norm and chunks[c.dst].norm:
                    G.add_edge(pydot.Edge(i, c.dst))
            G.write_png(f'./out44_{k}.png')
