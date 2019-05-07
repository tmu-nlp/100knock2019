#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

N = input()
N = int(N) 
path = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02"

with open(path + "\hightemp.txt", "r",encoding="utf-8") as file:
    readfile = file.read()
    file.seek(0)
    listfile = readfile.split("\n")
    file.seek(0)
    filenumber = len(file.readlines())

count = 0
ans = [[0]*100]*100

lim = int(filenumber / N)

for i in range(N):
    for j in range(lim):
        ans[i][j] = listfile[count]
        count+=1



for i in range(N):
    print("【分割第%d】" %(i+1))
    for j in range(lim):
        print(ans[i][j])