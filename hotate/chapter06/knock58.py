# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from collections import defaultdict
from typing import Generator, Tuple


def extract_svo(filename: str = './nlp.txt.xml') -> Generator[Tuple[str, str, str], None, None]:
    tree = ET.parse(filename)

    for sentence in tree.findall('.//sentences/sentence'):
        nsubj = defaultdict(str)  # 主語と述語の修飾関係
        dobj = defaultdict(str)  # 述語と直接目的語の修飾関係

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


def main():
    for s, v, o in extract_svo():
        print(s, v, o, sep='\t')


if __name__ == '__main__':
    main()
