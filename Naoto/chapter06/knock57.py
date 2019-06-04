'''
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，\
    係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''

import pydot
import xml.etree.ElementTree as ET


def coll(input_):
    count = 0
    count2 = 0
    color = 'green'
    tree = ET.parse(input_)
    root = tree.getroot()
    for deps in root.iter("dependencies"):
        if deps.attrib == {'type': 'collapsed-dependencies'}:
            G = pydot.Dot(graph_type='digraph')
            for gov, dep in zip(deps.iter("governor"), deps.iter("dependent")):
                gov_node = '"' + gov.text.rstrip() + '"'
                dep_node = '"' + dep.text.rstrip() + '"'
                # print(gov_node, dep_node)
                gov_num = gov.attrib["idx"]
                dep_num = dep.attrib["idx"]
                # print(gov_num, dep_num)
                G.add_node(pydot.Node(gov_num, label=gov_node, color=color))
                G.add_node(pydot.Node(dep_num, label=dep_node, color=color))
                G.add_edge(pydot.Edge(gov_num, dep_num))
            G.write_png(f"graph_{count2}.png")
            # print(1)
            count2 += 1
            # print(count2)


if __name__ == "__main__":
    input_ = "nlp.txt.xml"
    coll(input_, output_)
