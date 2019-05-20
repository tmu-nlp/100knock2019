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
    '''
    参考 : https://teratail.com/questions/75353
    *count : countをアンパック(tupleのみを取り出す)
    zip(*count) : 引数で渡されたそれぞれの要素を集めたtupleのイテレータを作る。
    '''
    histgram = list(zip(*count))[1]  # 0は単語名

    plt.hist(histgram, bins=20, range=(1, 20))  # bins : 棒の数  range : 横軸の範囲、この場合出現頻度
    plt.xlim(left=1, right=20)
    fp = FontProperties(fname=r'/mnt/c//Windows/Fonts/ipaexg.ttf')
    plt.xlabel('出現頻度', fontproperties=fp)
    plt.ylabel('単語の種類数', fontproperties=fp)

    plt.show()


if __name__ == '__main__':
    main()

