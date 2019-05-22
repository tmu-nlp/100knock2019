from knock30 import importmecab
import knock36 as knock36
import matplotlib.pyplot as plt

# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
# これ問題を勘違いしてるわー


def zipf(wdict: dict):

    # sort word dictionary
    sortwords = sorted(
                wdict.items(),
                key=lambda x: x[1],
                reverse=True)

    # タイプとカウントを、タプルのリストから取り出す
    # 参考：https://stackoverflow.com/questions/4800811/accessing-a-value-in-a-tuple-that-is-in-a-list
    counts = [x[1] for x in sortwords]

    # タイプ数
    N = len(counts)

    # 両対数グラフ
    plt.loglog(range(1, N+1), counts)

    plt.show()

    return None


def main():
    path = 'neko.txt.mecab'
    wdict = knock36.hist_words(importmecab(path))
    zipf(wdict)


if __name__ == '__main__':
    main()