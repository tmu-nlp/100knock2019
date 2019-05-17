'''
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形\
    （surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，\
    1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''


def morphines_read():
    from collections import defaultdict
    import re
    morphines = []
    morphines_dic = defaultdict(lambda: 0)
    sentences = {}
    morphines_list = []
    with open("neko.txt.mecab", "r") as mecab:
        for line in mecab:
            if not("EOS" in line):
                details = re.split("[\t,]", line.rstrip())
                morphines_list.append(details[0])
                morphines_dic = {"surface": details[0], "base": details[7],\
                    "pos": details[1], "pos1": details[2]}
                morphines.append(morphines_dic)
            elif len(morphines_list) != 0:
                sentences["".join(morphines_list)] = morphines_list
                morphines_list = []
            else:
                morphines_list = []
    return morphines, sentences


if __name__ == "__main__":
    morphines, sentences = morphines_read()
    print(morphines[0:16])