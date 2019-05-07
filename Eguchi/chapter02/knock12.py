##各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．


import re
path = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02"
filename = r"\hightemp.txt"
with open( path + filename, "r",encoding="utf-8" ) as file:

    readfile = file.read()
    readfile = readfile.split("\n")

    file.seek(0)
    NumLin = len(file.readlines())
    file.seek(0)

    firstword = ""
    secondword = ""
    for i in  range(NumLin ):
        firstword += readfile[i][0]+"\n"
        secondword += readfile[i][1] + "\n"



with open(path + r"\col1.txt", mode = "w")as col1:
    col1.write(firstword)

with open(path + r"\col2.txt", mode = "w") as col2:
    col2.write(secondword)


