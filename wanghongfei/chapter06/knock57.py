import xml.etree.ElementTree as ET
from graphviz import Digraph

xml_tree = ET.parse("./nlp.txt.xml")
sentences = []
for dependency in xml_tree.iter("dependencies"):
    if dependency.get("type") == "collapsed-dependencies":
        sentence_dependency = []
        for dep in dependency.iter("dep"):
            governor = dep.find("governor").text
            dependent = dep.find("dependent").text
            if dependent != "." and dependent != ",":
                sentence_dependency.append((governor, dependent))
        sentences.append(sentence_dependency)

G = Digraph(format = "png")
G.attr("node", shape = "circle")
for edge in sentences[6]:
    G.edge(edge[0], edge[1])
G.render("Collapsed Dependencies")
