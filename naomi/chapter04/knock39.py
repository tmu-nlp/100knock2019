from knock30 import importmecab
import knock36 as knock36
import matplotlib.pyplot as plt

# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．


def showhist10(wdict: dict):

    # sort word dictionary
    sortwords = sorted(
                wdict.items(),
                key=lambda x: x[1],
                reverse=True)

    # 上位１０の単語を、タプルのリストから取り出す
    # 参考：https://stackoverflow.com/questions/4800811/accessing-a-value-in-a-tuple-that-is-in-a-list
    words = [x[0] for x in sortwords]
    counts = [x[1] for x in sortwords]

    # タイプ数
    N = len(words)
    # フォント指定
    plt.rcParams['font.family'] = 'AppleGothic'

    # 棒グラフ
    plt.barh(range(N), counts, align='center')

    # Y軸にラベル
    plt.yticks(range(N), words)

    plt.show()

    print(words)

    return None


def main():
    path = 'neko.txt.mecab'
    wdict = knock36.hist_words(importmecab(path))
    showhist10(wdict)


if __name__ == '__main__':
    main()
