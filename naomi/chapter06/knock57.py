import xml.etree.ElementTree as ET
from collections import defaultdict
import pydot

def make_graph(edges: list) -> pydot.Dot:
    # edges = [((識別子１, ラベル１),(識別子２、ラベル２)), ...]

    # 有向グラフとして作成
    mydot = pydot.Dot(graph_type='digraph')

    for edge in edges:

        # ノード１
        node1 = str(edge[0][0])
        label1 = str(edge[0][1])

        # ノード２
        node2 = str(edge[1][0])
        label2 = str(edge[1][1])

        # ノードを追加
        mydot.add_node(pydot.Node(node1, label=label1))
        mydot.add_node(pydot.Node(node2, label=label2))

        # エッジ（ノード１→ノード２）を追加
        mydot.add_edge(pydot.Edge(node1, node2))

    return mydot


def make_edges(path: str) -> list:

    tree = ET.parse(path)
    root = tree.getroot()


    for sentence in root.iterfind('./document/sentences/sentence'):
        sid = int(sentence.get('id'))

        edges = []

        for dep in sentence.iterfind(
            './dependencies[@type="collapsed-dependencies"]/dep'
        ):

            if dep.get('type') != 'punct':
                govr = dep.find('./governor')
                dept = dep.find('./dependent')
                edges.append(
                    ((govr.get('idx'), govr.text), (dept.get('idx'), dept.text))
                )

    return edges



def main():
    inpath = 'nlp.txt.xml'
    edges = make_edges(inpath)
    mygraph = make_graph(edges)
    mygraph.write(path='./57.png', format='png')


if __name__ == '__main__':
    main()

# java -mx5g -cp "./*" 
# edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,
# lemma,ner,parse,dcoref -file nlp.txt  --add-modules java.se.ee;
