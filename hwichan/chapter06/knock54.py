import xml.etree.ElementTree as ET


def main():
    root = ET.parse('nlp.txt.xml')  # xmlを解析
    # root.iter() : 指定されたタグを持つノードのみに処理を絞り込む。
    # tokenには ElementTree インスタンスが返される。
    for i, token in enumerate(root.iter('token')):
        if i == 50:
            break
        word = token.findall('word')[0].text
        lemma = token.findall('lemma')[0].text
        pos = token.findall('POS')[0].text
        print('{}\t{}\t{}'.format(word, lemma, pos))


if __name__ == '__main__':
    main()
