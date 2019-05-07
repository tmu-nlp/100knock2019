# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ

from knock30 import load_morpheme_list
from collections import defaultdict
from typing import List, Dict, Tuple

M = List[Dict[str, str]]

def get_word_frequency(morphemes: M) -> Dict[str, int]:
    frequency = defaultdict(int) # type: Dict[str, int]
    for m in morphemes:
        frequency[m["surface"]] += 1
    return frequency

if __name__ == "__main__":
    print(get_word_frequency(load_morpheme_list()))