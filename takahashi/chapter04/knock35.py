# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

from knock30 import load_morpheme
from typing import List, Dict

M = List[Dict[str, str]]
T = List[M]


def get_consecutive_nouns(morphemes: T) -> List[str]:
    consecutive_nouns = []  # type: List[str]
    for sentence in morphemes:
        nouns = []
        for morpheme in sentence:
            if morpheme["pos"] == "名詞":
                nouns.append(morpheme["surface"])
            else:
                if len(nouns) > 1:
                    consecutive_nouns.append("".join(nouns))
                nouns = []
    return consecutive_nouns


if __name__ == "__main__":
    for noun in get_consecutive_nouns(load_morpheme()):
        print(noun)
