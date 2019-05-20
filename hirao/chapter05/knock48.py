from knock41 import load_chunk_list
import re
from graphviz import Digraph
import pydot_ng as pydot
from PIL import Image

pattern = re.compile('([\d,.，、．。, ]+)')


def visualization(sentence):
    # 一応有向グラフも作る
    graph = pydot.Dot(graph_type='digraph')
    for source_chunk in sentence:
        s = pattern.sub("", source_chunk.morphstr)
        if "名詞" in [x.pos for x in source_chunk.morphs]:
            source_idx = source_chunk.index
            dst = source_chunk.dst
            # 名詞から最後まで辿る
            while dst != -1:
                s += " -> {}".format(pattern.sub("", sentence[dst].morphstr))
                graph.add_node(pydot.Node(source_idx,
                                          label=pattern.sub("", sentence[source_idx].morphstr)))
                graph.add_node(pydot.Node(dst,
                                          label=pattern.sub("", sentence[dst].morphstr)))
                graph.add_edge(pydot.Edge(source_idx, dst))
                source_idx = dst
                dst = sentence[dst].dst
            print(s)

    graph.write_png('knock48.png')


if __name__ == "__main__":
    sentence_list = load_chunk_list("neko.txt.cabocha")
    visualization(sentence_list[5])
Image.open('knock48.png')
'''
吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
'''
