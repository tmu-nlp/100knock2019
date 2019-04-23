from knock30 import load_txt
import collections
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# font path
fp = FontProperties(fname='/Users/reo/Library/Fonts/Ricty-Regular.ttf')

word_list = load_txt("neko.txt.mecab")
words = list(map(lambda x: x["surface"], word_list))
counter = collections.Counter(words).most_common()
y = list(map(lambda x: x[1], counter))
x = list(range(1, len(y)+1))

plt.scatter(x, y)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("出現頻度順位", fontproperties=fp)
plt.ylabel("出現頻度", fontproperties=fp)
plt.show()