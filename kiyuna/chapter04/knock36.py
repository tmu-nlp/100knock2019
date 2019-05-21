'''
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
'''
import sys
from collections import Counter
from knock30 import mecab_into_sentences


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


if __name__ == '__main__':
    tgt = '形態素'
    cnter = Counter()
    for sentence in mecab_into_sentences():
        cnter += Counter(d['surface'] for d in sentence)
    res = [k for k, v in cnter.most_common()]
    print(res)
    message(f'{tgt}の種類: {len(cnter)}')
