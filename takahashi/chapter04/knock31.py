# 31. 動詞
# 動詞の表層形をすべて抽出せよ．

from knock30 import load_morpheme_list
from typing import List, Dict

M = List[Dict[str, str]]


def get_verbs(morphemes: M) -> List[str]:
    verbs = []  # type: List[str]
    for morpheme in morphemes:
        if morpheme["pos"] == "動詞":
            verbs.append(morpheme["surface"])
    return verbs


if __name__ == "__main__":
    for verb in get_verbs(load_morpheme_list()):
        print(verb)
