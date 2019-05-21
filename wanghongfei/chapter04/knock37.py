from knock30 import get_morph
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
result = get_morph("/Users/hongfeiwang/100knock2019/wanghongfei/chapter04/neko.txt.mecab")
frequency = {}
for sentence in result:
    for morph in sentence:
        frequency.setdefault(morph["基本形"], 0)
        frequency[morph["基本形"]] += 1
frequency_sorted = sorted(frequency.items(), key=lambda x:x[1])

x = [ i[0] for i in frequency_sorted[-10:] ]
y = [ i[1] for i in frequency_sorted[-10:] ]
plt.bar(x,y,align = 'center')
plt.title("words frequency top 10")
plt.ylabel("frequency")
plt.xlabel("words")
plt.show()