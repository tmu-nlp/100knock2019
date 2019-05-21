from knock30 import get_morph
import numpy as np
from matplotlib import pyplot as plt
result = get_morph("/Users/hongfeiwang/100knock2019/wanghongfei/chapter04/neko.txt.mecab")
frequency = {}
for sentence in result:
    for morph in sentence:
        frequency.setdefault(morph["基本形"], 0)
        frequency[morph["基本形"]] += 1
frequency_sorted = sorted(frequency.items(), key=lambda x:x[1])

a = np.array([ i[1] for i in frequency_sorted ])
group = [0,2,4,6,8,10] 
np.histogram(a,bins=group)
hist,bins = np.histogram(a,bins=group)
print(hist,bins)
plt.hist(a,bins=group)
plt.title("histogram of words frequency")
plt.show()

