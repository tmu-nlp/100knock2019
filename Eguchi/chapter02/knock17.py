##1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．


path = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02"

with open(path + "\hightemp.txt", "r",encoding="utf-8") as file:
    readfile = file.read()
    listfile = readfile.split("\n")
    file.seek(0)
    filenumber = len(file.readlines())

ans=[]

for i in listfile:
    ans.append(i.split("\t"))

for i in range(filenumber):
    print(ans[i][0])
    