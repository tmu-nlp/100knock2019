##自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

N = input()
N = int(N) + 1

path = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02"

with open(path + "\hightemp.txt", "r",encoding="utf-8") as file:
    readfile = file.read()
    file.seek(0)
    listfile = readfile.split("\n")


for i in range(1,N+1):
    print(listfile[-i])

