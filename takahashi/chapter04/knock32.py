# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．

from knock30 import load_morpheme_list
from typing import List, Dict

M = List[Dict[str, str]]


def get_base_form_verbs(morphemes: M) -> List[str]:
    verbs = []  # type: List[str]
    for morpheme in morphemes:
        if morpheme["pos"] == "動詞":
            verbs.append(morpheme["base"])
    return verbs


if __name__ == "__main__":
    for verb in get_base_form_verbs(load_morpheme_list()):
        print(verb)
