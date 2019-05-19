'''
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ
'''


import matplotlib.pyplot as mpt
import numpy as np
import math
from knock36 import word_frequency


def zipf_law():
    word_freq_dic = word_frequency()
    word_freq_list = sorted(word_freq_dic.values(), reverse=True)
    # x_math_gen = (math.log(i, log_scale) for i in range(1, len(word_freq_list)+1))
    # y_math_gen = (math.log(i, log_scale) for i in word_freq_list)
    x = [i for i in range(len(word_freq_list))]
    # print(x[0:20])
    # print(y[0:20])
    mpt.bar(x, word_freq_list, log=True)
    mpt.show()


if __name__ == "__main__":
    zipf_law()