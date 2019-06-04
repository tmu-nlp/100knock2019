import xml.etree.ElementTree as ET
from collections import defaultdict
from itertools import islice
from typing import Any, DefaultDict

from graphviz import Digraph


def load_coll_dep(filename: str = './nlp.txt.xml') -> DefaultDict[Any, list]:
    tree = ET.parse(filename)

    sentences = defaultdict(list)

    for sentence in tree.findall('.//sentences/sentence'):
        for dep in sentence.findall('./*[@type="collapsed-dependencies"]/dep'):
            no = f'[{sentence.attrib["id"]}]'
            governor = no + ' ' + dep.find('governor').text  # 係り元
            dependent = no + ' ' + dep.find('dependent').text  # 係り先
            sentences[no].append([governor, dependent])

    return sentences


def main(stop):
    sentences = load_coll_dep()

    G = Digraph(format='png')
    G.attr('node', shape='circle')

    for i, sentence in islice(sentences.items(), stop):
        for pair in sentence:
            G.edge(pair[0], pair[1])
    G.render('binary_tree_graphviz')


if __name__ == '__main__':
    main(3)
