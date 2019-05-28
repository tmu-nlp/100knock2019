# 59. S式の解析
# Stanford Core NLPの句構造解析の結果（S式）を読み込み，
# 文中のすべての名詞句（NP）を表示せよ．
# 入れ子になっている名詞句もすべて表示すること．

import xml.etree.ElementTree as ET
from nltk.tree import ParentedTree


def analyze_s_expression() -> None:
    root = ET.parse("../data/nlp.txt.xml")
    for s_exp in root.iterfind("./document/sentences/sentence/parse"):
        # S 式の文字列から tree を作成する
        tree = ParentedTree.fromstring(s_exp.text)
        for sub in tree.subtrees():
            # 名詞句の場合、その葉をすべて表示する
            if sub.label() == "NP":
                print(" ".join(list(sub.leaves())))


if __name__ == "__main__":
    analyze_s_expression()
