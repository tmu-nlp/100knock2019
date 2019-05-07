##12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
path = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02"

with open(path + r"\col1.txt", mode = "r")as col1:
    col1list = col1.read().split("\n")




with open(path + r"\col2.txt", mode = "r") as col2:
    col2list = col2.read().split("\n")

output =""
for first, second in zip(col1list, col2list):
    output += first + "\t" + second +"\n"

print(output)

with open(path + r"\output.txt", mode ="w") as outputfile:
    outputfile.write(output)
