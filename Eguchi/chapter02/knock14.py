#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ

N = input()
N = int(N)

path = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02"

with open(path + "\hightemp.txt", "r",encoding="utf-8") as file:
    readfile = file.read()
    print(readfile)

    file.seek(0)
    listfile = readfile.split("\n")


for i in range(N):
    print(listfile[i])





