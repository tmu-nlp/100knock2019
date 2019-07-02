#Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
import re
import xml.etree.ElementTree as ET
from graphviz import Digraph

path = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt"
path2 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt.xml"

def analyzer():
    tree = ET.parse(path2)
    root = tree.getroot()
    for sentence in root.iterfind("./document/sentences/sentence"):
        lineid =int(sentence.get("id"))
        dependlist = []

        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            if not dep.get("type") == "punct":
                governor = dep.find('./governor')
                dependent = dep.find("./dependent")
                dependlist.append(((governor.get("idx"),governor.text),(dependent.get("idx"),dependent.text)))

        Gragh = dot_make( dependlist)
        Gragh.render("{}.tree" .format(lineid))
            

def dot_make(dependlist):
    G = Digraph(format='png')
    G.attr('node', shape='circle')
    G.attr('node', fontname="MS Gothic")
    for word in dependlist:
        print("governor=%s dependent=%s" %(word[0][1], word[1][1]))
        id1 = word[0][0]
        label1 = word[0][1]
        id2 = word[1][0]
        label2 = word[1][1]
        G.node(id1, label=label1)
        G.node(id2, label=label2)
        G.edge(id1,id2)

    return G


#nlp_make()
dot_make(analyzer())