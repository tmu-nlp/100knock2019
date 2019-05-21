from knock30 import importmecab
import knock36 as knock36
import matplotlib.pyplot as plt

# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．


def showhist10(wdict: dict):

    # sort word dictionary
    sortwords = sorted(
                wdict.items(),
                key=lambda x: x[1],
                reverse=True)

    # タイプとカウントを、タプルのリストから取り出す
    # 参考：https://stackoverflow.com/questions/4800811/accessing-a-value-in-a-tuple-that-is-in-a-list
    words = [x[0] for x in sortwords[0:10]]
    counts = [x[1] for x in sortwords[0:10]]

    # フォント指定
    plt.rcParams['font.family'] = 'AppleGothic'

    # 棒グラフ
    plt.bar(range(10), counts, align='center')

    # X軸にラベル
    plt.xticks(range(10), words)

    plt.show()

    print(words)

    return None


def main():
    path = 'neko.txt.mecab'
    wdict = knock36.hist_words(importmecab(path))
    showhist10(wdict)


if __name__ == '__main__':
    main()
