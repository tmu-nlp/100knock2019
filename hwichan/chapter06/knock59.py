import xml.etree.ElementTree as ET
from nltk.tree import ParentedTree


def main():
    root = ET.parse('nlp.txt.xml')

    for parse in root.iterfind('./document/sentences/sentence/parse'):
        '''
        text = (NP (NP (DT the) (JJ free) (NN encyclopedia) (JJ Natural) (NN language) (NN processing))
               (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-)))
        ParentedTree.fromstring(text):
        (NP
          (NP
            (DT the)
            (JJ free)
            (NN encyclopedia)
            (JJ Natural)
            (NN language)
            (NN processing))
          (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-)))
        tree.subtrees() : tagごとにジェネレーターでテキストが返ってくる
        tree.label() : tag名
        tree.leaves() : 値(単語)のみを配列に格納
        '''
        tree = ParentedTree.fromstring(parse.text)
        for sub in tree.subtrees():
            if sub.label() == "NP":
                print(" ".join(sub.leaves()))


if __name__ == '__main__':
    main()
