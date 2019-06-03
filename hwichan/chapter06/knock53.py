from pycorenlp import StanfordCoreNLP
import xml.etree.ElementTree as ET


def parse_nlp():
    with open('nlp.txt', 'r') as f:
        text = f.read()

    nlp = StanfordCoreNLP("http://localhost:9000")
    output = nlp.annotate(text, properties={'timeout': '50000',
                                            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,dcoref',
                                            'outputFormat': 'xml'})
    # timeoutを設定しないと時間が短すぎてエラー、annotatorsはtextを解析する項目

    with open('nlp.txt.xml', 'w') as f:
        f.write(output)


def main():
    # parse_nlp()
    root = ET.parse('nlp.txt.xml')  # xmlを解析

    for i, word in enumerate(root.iter('word')):  # root.iter() : 指定されたタグを持つノードのみに処理を絞り込む
        if i == 50:
            break
        print(word.text)


if __name__ == '__main__':
    main()
