from knock30 import load_morpheme
from collections import defaultdict
from knock36 import calc_word_frequency
from matplotlib import pyplot as plt

path = 'neko.txt.mecab'
result = load_morpheme(path)
words_freq = calc_word_frequency(result)

plt.hist(words_freq.values(), bins=200)
plt.show()