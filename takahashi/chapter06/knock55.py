# 55. 固有表現抽出
# 入力文中の人名をすべて抜き出せ．

import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree = ET.parse("../data/nlp.txt.xml")
    for token in tree.iter("token"):
        # 固有表現は NER タグで出力されている
        if token.findtext("NER") == "PERSON":
            print(token.findtext("word"))
