from knock30 import load_txt
import collections
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# font path
fp = FontProperties(fname='/Users/reo/Library/Fonts/Ricty-Regular.ttf');

SIZE = 10

word_list = load_txt("neko.txt.mecab")
words = list(map(lambda x: x["surface"], word_list))
counter = collections.Counter(words).most_common()[:SIZE]

x = list(map(lambda x: x[0], counter))
y = list(map(lambda x: x[1], counter))
plt.bar(x, y)
xs = np.arange(len(x))
plt.xticks(xs, x, fontproperties=fp)
plt.xlabel("語", fontproperties=fp)
plt.ylabel("出現頻度", fontproperties=fp)
plt.show()