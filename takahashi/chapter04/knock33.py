# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．

from knock30 import load_morpheme_list
from typing import List, Dict

M = List[Dict[str, str]]

def get_sahen_noun(morphemes: M) -> List[str]:
    nouns = [] # type: List[str]
    for morpheme in morphemes:
        if morpheme["pos1"] == "サ変接続":
            nouns.append(morpheme["surface"])
    return nouns

if __name__ == "__main__":
    for noun in get_sahen_noun(load_morpheme_list()):
        print(noun)