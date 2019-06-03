'''
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（）を代表参照表現（representative mention）に置換せよ．\
    ただし，置換するときは，「代表参照表現（mention参照表現）」のように，元の参照表現が分かるように配慮せよ．
'''

import xml.etree.ElementTree as ET


def representative_mention(input_, output_):
    count = 0
    with open(output_, "w") as fw:
        tree = ET.parse(input_)
        root = tree.getroot()
        for mention in root.iter("mention"):
            if mention.attrib == {'representative': 'true'}:
                mention_re = mention[4].text
            else:
                print(f"{mention[4].text}({mention_re})", file=fw)


if __name__ == "__main__":
    input_ = "nlp.txt.xml"
    output_ = "mention_56.txt"
    representative_mention(input_, output_)