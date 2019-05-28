# 54. 品詞タグ付け
# Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree = ET.parse("../data/nlp.txt.xml")

    # token を抽出し、その中から word, lemma, pos を抜き出す
    for token in tree.iter("token"):
        word, lemma, pos = (
            token.findtext("word"),
            token.findtext("lemma"),
            token.findtext("POS"),
        )
        print(f"{word}\t{lemma}\t{pos}")
