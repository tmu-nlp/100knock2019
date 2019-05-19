'''
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''


import matplotlib.pyplot as mpt
from knock36 import word_frequency


def frequet_word_graph_n(n: str):
    word_freq_dic = word_frequency()
    word_freq_dic = sorted(word_freq_dic.items(), key=lambda x: x[1], reverse=True)
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


if __name__ == "__main__":
    frequet_word_graph_n(10)
