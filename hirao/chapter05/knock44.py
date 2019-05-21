from knock41 import load_chunk_list
import re
from graphviz import Digraph
import pydot_ng as pydot
from PIL import Image

pattern = re.compile('([\d,.，、．。,「」 ]+)')


def visualization(sentence):
    # 有向グラフ
    graph = pydot.Dot(graph_type='digraph')
    for chunk in sentence:
        # dstから辿る
        source_i = chunk.index
        target_i = chunk.dst
        graph.add_node(pydot.Node(source_i, label=pattern.sub(
            "", sentence[source_i].morphstr)))
        graph.add_node(pydot.Node(target_i, label=pattern.sub(
            "", sentence[target_i].morphstr)))
        graph.add_edge(pydot.Edge(source_i, chunk.dst))
    graph.write_png('knock44.png')


if __name__ == "__main__":
    sentence_list = load_chunk_list("neko.txt.cabocha")
    visualization(sentence_list[4])
Image.open('knock44.png')
