'''
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
'''
from collections import defaultdict
from matplotlib import pyplot as plt
from knock30 import get_morpheme_list

word_freq = defaultdict(lambda: 0)

for sentence in get_morpheme_list('neko.txt.mecab'):
    for morpheme in sentence:
        word_freq[morpheme['surface']] += 1


plt.rcParams['font.family'] = 'AppleGothic'
plt.loglog(
    range(1, len(word_freq) + 1),
    sorted(word_freq.values(), reverse=True)
)
plt.title("Zipfの法則")
plt.xlabel('出現度順位')
plt.ylabel('出現頻度')

plt.show()