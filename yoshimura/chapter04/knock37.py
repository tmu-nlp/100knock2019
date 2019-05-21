'''
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''
from collections import defaultdict
from matplotlib import pyplot as plt
from knock30 import get_morpheme_list

word_freq = defaultdict(lambda: 0)

for sentence in get_morpheme_list('neko.txt.mecab'):
    for morpheme in sentence:
        word_freq[morpheme['surface']] += 1

d = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

words = [d[i][0] for i in range(10)]
count = [d[i][1] for i in range(10)]

plt.rcParams['font.family'] = 'AppleGothic'
plt.bar(words, count)
plt.xlabel("出現頻度が高い10語")
plt.ylabel("出現頻度")
plt.grid(True)
plt.show()
