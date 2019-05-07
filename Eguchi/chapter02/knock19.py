#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

import collections


path = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02"

with open(path + "\hightemp.txt", "r",encoding="utf-8") as file:
    readfile = file.read()
    listfile = readfile.split("\n")
    file.seek(0)
    filenumber = len(file.readlines())

ans=[]

for i in listfile:
    ans.append(i.split("\t"))

countlist= []
for i in range(filenumber):
    countlist.append(ans[i][0])
    

c = collections.Counter(countlist)

for i in c.most_common():
    print(i)

