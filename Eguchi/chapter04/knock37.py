#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．


import MeCab
import re
import collections
import pprint
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
sortwords = collections.Counter(countword)
sortwords = sorted(sortwords.items(), key=lambda x: -x[1])

xlabel = []
yhigh = []
x = []
for i, word  in enumerate(sortwords):
    xlabel.append(word[0]) 
    yhigh.append(word[1])
    x.append(i)
    if i == 10:
        break

w = 0.3

plt.bar(x,yhigh, width=w)
plt.xticks(x, xlabel, FontProperties=fp)
plt.show()
