'''
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''


import matplotlib.pyplot as mpt
from knock30 import morphines_read
from knock36 import word_frequency


def frequet_word_graph_n(n: str):
    morphines, sentences = morphines_read()
    word_freq_dic = word_frequency()
    count = 0
    x = []
    y = []
    for k, v in word_freq_dic:
        if count == n:
            break
        else:
            x.append(k)
            y.append(v)
        count += 1
    mpt.bar(x, y)
    mpt.show()
    # print(x)
    # print(y)


if __name__ == "__main__":
    frequet_word_graph_n(10)
