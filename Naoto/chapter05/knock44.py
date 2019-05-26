'''
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，\
    Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''

from knock40 import Morph
from knock41 import Chunk
from knock41 import cabocha_Chunk_read
import pydot


def gen_graph(edges):
    graph = pydot.Dot(graph_type='digraph')
    graph.set_node_defaults(fontname='Sans Not-Rotated 12')

    for edge in edges:
        id1 = str(edge[0])
        label1 = edge[1]
        id2 = str(edge[2])
        label2 = edge[3]

        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))
        # ノードを作らずにエッジだけでも動く(下で言うidがそのまま名前になる。名前の被りには注意)

        graph.add_edge(pydot.Edge(id1, id2))
    return graph


def main():
    for i, chunks in enumerate(cabocha_Chunk_read()):
        if i < 7:
            continue
        if i > 7:
            break
        edges = []
        for j, chunk in enumerate(chunks):
            if chunk.dst == -1:
                continue
            src = chunk.normalized_surface()
            dst = chunks[chunk.dst].normalized_surface()
            if not src or not dst:
                continue
            edges.append((j, src, chunk.dst, dst))

        # グラフの書き出し
        graph = gen_graph(edges)
        print(graph.to_string())
        graph.write('graph.png', format='png', encoding='utf8')


if __name__ == "__main__":
    main()
