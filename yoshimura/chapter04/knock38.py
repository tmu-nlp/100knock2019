'''
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
'''
from collections import defaultdict
from matplotlib import pyplot as plt
from knock30 import get_morpheme_list

word_freq = defaultdict(lambda: 0)

for sentence in get_morpheme_list('neko.txt.mecab'):
    for morpheme in sentence:
        word_freq[morpheme['surface']] += 1

plt.hist(word_freq.values(), bins=20, range=(1, 20))
plt.xticks(range(1, 21))
plt.xlim(1, 20)
plt.show()
