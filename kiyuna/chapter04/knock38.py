'''
38. ヒストグラム
単語の出現頻度のヒストグラム
（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
'''
from matplotlib import pyplot as plt
from collections import Counter
from knock30 import mecab_into_sentences


if __name__ == '__main__':
    num = None
    cnter = Counter()
    for sentence in mecab_into_sentences():
        cnter += Counter(d['surface'] for d in sentence)

    _, data = zip(*cnter.most_common(num))
    plt.hist(data, bins=range(45))
    plt.title("ヒストグラム")
    plt.xlabel("出現頻度")
    plt.ylabel("単語の種類数")
    plt.savefig('out38.png')
