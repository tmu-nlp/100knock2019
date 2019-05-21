##単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
import MeCab
import re
from collections import Counter
import pprint
import collections
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname=r'C:\Windows\Fonts\msgothic.ttc', size=14)


def openmecab():
    inputname = r"\Users\Koya\Documents\Lab\neko.txt.mecab"
    with open( inputname, mode = "r",encoding="utf-8")as inputfile:
        splitfile =inputfile.read().split("\n")
        return splitfile 

def splitmecab(sentence):
    l = []
    for line in sentence:
        if ( r"-" in line):
            line = re.sub("-","\t",line)  ##['吾輩', 'ワガハイ', '吾輩', '名詞-代名詞-一般', '', '']
        l.append(line.split("\t"))


    dictlist =[]
    for i in range(len(l)-2):
        dictwords = {
            "surface": l[i][0],
            "base":l[i][2],
            "pos":l[i][3],
            "pos1":l[i][4]
            }
        dictlist.append(dictwords)
    return dictlist


sentence = openmecab()
mecabfile = splitmecab(sentence)

countword = []
for line in mecabfile:
    countword.append(line["surface"])

countword = collections.Counter(countword)
countword = countword.most_common()
countword = list(zip(*countword))[1]
print(countword)
"""
[('の', 9194), ('。', 7486), ('て', 6873), ('、', 6772), ('は', 6422), ('に', 6268), ('を', 6071), ('と', 5515), ('が', 5339), ('た', 3989),
('で', 3813), ('「', 3231), ('」', 3225), ('も', 2479), ('ない', 2391), ('だ', 2367), ('し', 2328), ('から', 2043), ('ある', 1730), ('な', 1612), 
"""

plt.hist( countword, bins=20, range=(1, 20), normed=True)
plt.xlim(xmin=1, xmax=20)
plt.xlabel('出現頻度', fontproperties=fp)
plt.ylabel('単語の種類数', fontproperties=fp)
plt.show()
