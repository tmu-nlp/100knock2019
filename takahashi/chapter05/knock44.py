# 44. 係り受け木の可視化
# 与えられた文の係り受け木を有向グラフとして可視化せよ．

from knock41 import load_chunk_cabocha, Chunk
from typing import List
import pydot
import sys


def visualize_dependency_tree(chunks: List[Chunk], file="dependency_tree.png") -> None:
    graph = pydot.Dot(graph_type="digraph")  # グラフを有向グラフにする
    edges, nodes = [], []
    # src, dst のタプルのリスト (edge) を作成する
    for chunk in chunks:
        nodes.append(chunk.no_symbols())
        if chunk.dst == -1:
            continue

        src = chunk.no_symbols()
        dst = chunks[chunk.dst].no_symbols()
        if src != "" and dst != "":
            edges.append((src, dst))

    # node の追加
    for node in nodes:
        graph.add_node(pydot.Node(node, label=node))

    # edge の追加
    for edge in edges:
        graph.add_edge(pydot.Edge(edge[0], edge[1]))

    graph.write_png(file)


# n 番目の文の係り受け木を作成する
def main(n=10) -> None:
    chunks_list = load_chunk_cabocha()
    visualize_dependency_tree(chunks_list[n])


if __name__ == "__main__":
    args = sys.argv
    main(int(args[1]))
