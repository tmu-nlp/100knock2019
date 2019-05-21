'''
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
'''
from collections import defaultdict
from operator import itemgetter
from knock30 import get_morpheme_list

word_freq = defaultdict(lambda: 0)

for sentence in get_morpheme_list('neko.txt.mecab'):
    for morpheme in sentence:
        word_freq[morpheme['surface']] += 1

for word, freq in sorted(word_freq.items(), key=itemgetter(1), reverse=True):
    print(f'{word}\t{freq}')
