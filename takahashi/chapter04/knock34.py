# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ

from knock30 import load_morpheme_list
from typing import List, Dict

M = List[Dict[str, str]]

def get_noun_phrases(m: M) -> List[str]:
    noun_phrases = []
    for i in range(len(m) - 2):
        if m[i]["pos"] == m[i+2]["pos"] == "名詞" and m[i+1]["surface"] == "の":
            noun_phrases.append(m[i]["surface"] + m[i+1]["surface"] + m[i+2]["surface"])
    return noun_phrases

if __name__ == "__main__":
    for noun_phrase in get_noun_phrases(load_morpheme_list()):
        print(noun_phrase)