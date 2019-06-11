import xml.etree.ElementTree as ET
from collections import defaultdict
from typing import Generator, Tuple
import pydot


def ext_svo(path: str) -> Generator[Tuple[str, str, str], None, None]:

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
                edges.append((
                    (govr.get('idx'), govr.text), (dept.get('idx'), dept.text)
                ))

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
