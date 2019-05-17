from knock30 import load_txt
import collections
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
# Japanese font path
fp = FontProperties(fname='/Users/reo/Library/Fonts/Ricty-Regular.ttf')

SIZE = 10

sentence_list = load_txt("neko.txt.mecab")
# 文である必要がないので、単語ごとにバラす(2次元 -> 1次元)
word_list = [flatten for inner in sentence_list for flatten in inner]
words = list(map(lambda x: x["surface"], word_list))
# counterを使う
counter = collections.Counter(words).most_common()[:SIZE]

# x軸とy軸に値を入れる
x = list(map(lambda x: x[0], counter))
y = list(map(lambda x: x[1], counter))
# 棒グラフ用のbar
plt.bar(x, y)
# rangeと同じ等差数列用の関数
xs = np.arange(len(x))
plt.xticks(xs, x, fontproperties=fp)
# ラベル名
plt.xlabel("語", fontproperties=fp)
plt.ylabel("出現頻度", fontproperties=fp)

plt.show()