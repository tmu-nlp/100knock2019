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

plt.hist(y, bins=30, range=(1, 30))
plt.xlabel("出現頻度", fontproperties=fp)
plt.ylabel("単語の種類数", fontproperties=fp)
plt.show()