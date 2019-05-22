# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ

from knock30 import load_morpheme_list
from collections import defaultdict
from typing import List, Dict, Tuple, Iterable
from operator import itemgetter

M = List[Dict[str, str]]


def get_word_frequency(morphemes: M) -> Iterable[Tuple[str, int]]:
    frequency = defaultdict(int)  # type: Dict[str, int]
    for m in morphemes:
        frequency[m["surface"]] += 1
    return sorted(frequency.items(), key=itemgetter(1), reverse=True)


if __name__ == "__main__":
    print(get_word_frequency(load_morpheme_list()))
