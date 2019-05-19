'''
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
'''


import matplotlib.pyplot as mpt
from knock36 import word_frequency


def frequency_word_histgram():
    word_freq_dic = word_frequency()
    word_freq_list = sorted(word_freq_dic.values())
    mpt.hist(word_freq_list)
    mpt.show()


if __name__ == "__main__":
    frequency_word_histgram()