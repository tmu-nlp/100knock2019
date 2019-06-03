import xml.etree.ElementTree as ET


def main():
    root = ET.parse('nlp.txt.xml')  # xmlを解析
    # root.iter() : 指定されたタグを持つノードのみに処理を絞り込む。
    # tokenには ElementTree インスタンスが返される。
    for token in root.iter('token'):
        # NERは固有表現の解析結果 wikipedia -> organization
        if token.findall("NER")[0].text == "PERSON":
            print(token.findall("word")[0].text)


if __name__ == '__main__':
    main()
