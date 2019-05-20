import MeCab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
m = MeCab.Tagger()


def make_list(filename: str) -> list:
    neko_list = []  # すべての文が格納
    neko_line = []  # 1文の形態素
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n').split('\t')  # 単語(表層形)と解析結果で分割
            if len(line) > 1:  # EOSは含まない
                cal1 = line[0]
                cal2 = line[1].split(',')
                neko_dict = {'surface': cal1, 'base': cal2[6], 'pos': cal2[0], 'pos1': cal2[1]}

                if neko_dict['surface'] == '。':  # '。'が文の終わりと判断
                    neko_line.append(neko_dict)
                    neko_list.append(neko_line)
                    neko_line = []
                else:
                    neko_line.append(neko_dict)

    return neko_list


def main():
    neko_list = make_list('neko.txt.mecab')
    count = {}
    for line in neko_list:
        for n, word in enumerate(line):
            count[word['surface']] = count.get(word['surface'], 0) + 1

    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    left = [i for i in range(0, 10)]  # 横軸、上位１０位まで
    height = []  # 縦軸、単語の出現数
    label = []  # 単語の名前
    for i, j in enumerate(count):
        if i == 10:
            break
        label.append(j[0])
        height.append(j[1])

    # fp = FontProperties(fname='/mnt/c//Windows/ontsHGRME.TTC', size=14)
    fp = FontProperties(fname=r'/mnt/c//Windows/Fonts/ipaexg.ttf')

    # print(label)
    # print(height)
    # print(count[:10])

    # plt.bar(left, height, tick_label = label)  # font指定はできない
    plt.bar(left, height)  # bar : 棒グラフ
    plt.xticks(left, label, fontproperties=fp)
    plt.show()


if __name__ == '__main__':
    main()

