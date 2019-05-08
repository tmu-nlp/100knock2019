# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from collections import defaultdict


def extract_svo(filename='./nlp.txt.xml'):
    tree = ET.parse(filename)

    for sentence in tree.findall('.//sentences/sentence'):
        nsubj = defaultdict(str)
        dobj = defaultdict(str)

        for dep in sentence.findall('./*[@type="collapsed-dependencies"]/dep'):
            governor = dep.find('governor').text
            dependent = dep.find('dependent').text

            if dep.attrib['type'] == 'nsubj':
                nsubj[governor] = dependent
            elif dep.attrib['type'] == 'dobj':
                dobj[governor] = dependent

        for gov, dep in nsubj.items():
            # nsubj, dobj の両方に関係がある場合，svo が読み取れる
            if dobj[gov]:
                s = dep
                v = gov
                o = dobj[gov]
                yield s, v, o


if __name__ == '__main__':
    for s, v, o in extract_svo():
        print(s, v, o, sep='\t')
