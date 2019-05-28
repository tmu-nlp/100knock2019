# 53. Tokenization
# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
# また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree = ET.parse("../data/nlp.txt.xml")
    # 単語を切り出せば良いので、word タグを選択する
    for word in tree.iter("word"):
        print(word.text)
