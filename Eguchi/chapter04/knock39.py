#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ
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

"""
[('の', 9194), ('。', 7486), ('て', 6873), ('、', 6772), ('は', 6422), ('に', 6268), ('を', 6071), ('と', 5515), ('が', 5339), ('た', 3989),
('で', 3813), ('「', 3231), ('」', 3225), ('も', 2479), ('ない', 2391), ('だ', 2367), ('し', 2328), ('から', 2043), ('ある', 1730), ('な', 1612), 
"""

plt.scatter(range(1, len(countword)+1), countword)

plt.xscale("log")
plt.yscale("log")
#plt.xlim(xmin=1, xmax=20)
plt.xlabel('単語の出現頻度順位', fontproperties=fp)
plt.ylabel('単語の出現頻度', fontproperties=fp)
plt.grid(axis = "both")

plt.show()