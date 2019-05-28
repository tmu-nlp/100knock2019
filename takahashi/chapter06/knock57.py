# 57. 係り受け解析
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を
# 有向グラフとして可視化せよ

import xml.etree.ElementTree as ET
from itertools import islice
import pydot


def collapsed_dependencies(n=0, file="./results/collapsed_dependencies.png") -> None:
    graph = pydot.Dot(graph_type="digraph")
    tree = ET.parse("../data/nlp.txt.xml")
    for sentence in islice(tree.iterfind("./document/sentences/sentence"), n, n + 1):
        for dep in sentence.iterfind(
            "./dependencies[@type='collapsed-dependencies']/dep"
        ):
            if dep.get("type") != "punct":
                g = dep.find("./governor")
                d = dep.find("./dependent")

                g_index, d_index = g.get("idx"), d.get("idx")
                graph.add_node(pydot.Node(g_index, label=g.text))
                graph.add_node(pydot.Node(d_index, label=d.text))

                graph.add_edge(pydot.Edge(g_index, d_index))
    graph.write_png(file)


if __name__ == "__main__":
    collapsed_dependencies(n=1)
