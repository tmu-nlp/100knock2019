'''
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
'''

import xml.etree.ElementTree as ET


def NER_extract(input_, output_):
    count = 0
    with open(output_, "w") as fw:
        tree = ET.parse(input_)
        root = tree.getroot()
        for word, NER in zip(root.iter("word"), root.iter("NER")):
            if NER.text == "PERSON":
                print(word.text, file=fw)


if __name__ == "__main__":
    input_ = "nlp.txt.xml"
    output_ = "ner_55.txt"
    NER_extract(input_, output_)
