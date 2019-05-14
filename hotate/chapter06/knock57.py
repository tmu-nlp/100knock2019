from typing import Any

from graphviz import Digraph
import xml.etree.ElementTree as ET
from collections import defaultdict


def load_coll_dep(filename: str = './nlp.txt.xml') -> defaultdict[Any, list]:
    tree = ET.parse(filename)

    sentences = defaultdict(list)

    for sentence in tree.findall('.//sentences/sentence'):
        for dep in sentence.findall('./*[@type="collapsed-dependencies"]/dep'):
            no = f'[{sentence.attrib["id"]}]'
            governor = no + ' ' + dep.find('governor').text
            dependent = no + ' ' + dep.find('dependent').text
            sentences[no].append([governor, dependent])

    return sentences


if __name__ == '__main__':
    from itertools import islice

    sentences = load_coll_dep()

    G = Digraph(format='png')
    G.attr('node', shape='circle')

    for i, sentence in islice(sentences.items(), 5):
        for pair in sentence:
            G.edge(pair[0], pair[1])
    G.render('binary_tree_graphviz')