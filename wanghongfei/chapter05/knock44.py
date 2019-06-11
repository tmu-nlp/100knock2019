from knock41 import get_chunk
from graphviz import Digraph
import pydot

def src_dst_list(text):
    src_dst_list = []
    for sentence in text:
        pair = []
        for i in range(len(sentence)):
            srcs = sentence[i]
            if srcs.dst == -1:
                pass
            else:
                pair.append((srcs,dst))
        src_dst_list.append(pair)
    return src_dst_list

file_name = "./chapter05/neko.txt.cabocha"
sentences = get_chunk(file_name)
print(sentences[1:3])
G = Digraph(format="png")
G.attr("node", shape="circle")
edge = []
