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

    x = []  # 単語の出現頻度順位
    y = []  # 出現頻度
    rank = 1
    for i in count:
        x.append(rank)
        y.append(i[1])
        rank += 1

    plt.scatter(x, y)  # 散布図
    plt.xscale('log')  # 対数グラフ
    plt.yscale('log')
    plt.xlim(left=1)  # x軸の表示範囲を修正、原点を１に変更

    fp = FontProperties(fname=r'/mnt/c//Windows/Fonts/ipaexg.ttf')
    plt.xlabel('出現度順位', fontproperties=fp)
    plt.ylabel('出現頻度', fontproperties=fp)

    # fp = FontProperties(fname='/mnt/c//Windows/ontsHGRME.TTC', size=14)

    plt.show()


if __name__ == '__main__':
    main()

