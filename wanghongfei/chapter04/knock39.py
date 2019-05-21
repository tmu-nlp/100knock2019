from knock30 import get_morph
import numpy as np
from matplotlib import pyplot as plt
from scipy import special
result = get_morph("/Users/hongfeiwang/100knock2019/wanghongfei/chapter04/neko.txt.mecab")
frequency = {}
for sentence in result:
    for morph in sentence:
        frequency.setdefault(morph["基本形"], 0)
        frequency[morph["基本形"]] += 1
frequency_sorted = sorted(frequency.items(), key=lambda x:x[1])

s = np.array([ i[1] for i in frequency_sorted ])
a = 2
count,bins,ignored = plt.hist(s[s<10],10,density=True)
x = np.arange(1.,10.)
y = x**(-a)/special.zetac(a)
plt.plot(x,y/max(y),linewidth=2)
plt.show()
