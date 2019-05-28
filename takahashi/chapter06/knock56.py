# 56. 共参照解析
# Stanford Core NLPの共参照解析の結果に基づき，
# 文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
# ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

import xml.etree.ElementTree as ET
from typing import List, Dict, Tuple


def coreference_analysis() -> None:
    tree = ET.parse("../data/nlp.txt.xml")

    reference = {}  # type: Dict[Tuple[int, int], Tuple[int, str]]
    for coref in tree.iterfind("./document/coreference/coreference"):
        for mention in coref.iterfind("./mention"):
            if mention.get("representative") != None:
                # 代表参照表現の文字列
                represent = mention.findtext("text")
            else:
                # 参照表現の辞書を作成
                id = int(mention.findtext("sentence"))
                start = int(mention.findtext("start"))
                end = int(mention.findtext("end"))

                if not (id, start) in reference:
                    reference[(id, start)] = (end, represent)

    for sentence in tree.iterfind("./document/sentences/sentence"):
        sentence_id = int(sentence.get("id"))
        token_rest = 0
        for token in sentence.iterfind("./tokens/token"):
            token_id = int(token.get("id"))

            # 置換
            if token_rest == 0 and (sentence_id, token_id) in reference:
                tail, represent = reference[(sentence_id, token_id)]
                # 代表参照表現を Markdown の **強調** で置換した文字列を分かりやすくする
                print(f"**{represent}** (", end="")
                token_rest = tail - token_id

            # 括弧内の word を表示し, token_rest を消費していく
            print(token.findtext("word"), end="")
            if token_rest > 0:
                token_rest -= 1
                if token_rest == 0:
                    print(")", end="")
            print(" ", end="")
        print()


if __name__ == "__main__":
    coreference_analysis()
