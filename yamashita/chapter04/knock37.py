from knock30 import load_morpheme
from collections import defaultdict
from knock36 import calc_word_frequency
from matplotlib import pyplot as plt

path = 'neko.txt.mecab'
result = load_morpheme(path)
words_freq = calc_word_frequency(result)

dic = sorted(words_freq.items(), key = lambda x:x[1], reverse = True)
words = [dic[i][0] for i in range(10)]
counts = [dic[i][1] for i in range(10)]

plt.rcParams['font.family'] = 'AppleGothic'
plt.xlabel('出現頻度が高い10語')
plt.ylabel('出現頻度')
plt.bar(words,counts)
plt.show()