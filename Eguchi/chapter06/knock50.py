#(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
path = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt"

import re


def line_make():
    linelist = []
    with open(path,mode = "r",encoding='utf-8' ) as f:
        for line in f:
            line = re.sub(r"(?P<group>[.:;!?])(\s)(?P<group3>[A-Z])", r"\1\n\3", line )
            linelist.append(line)

    return linelist

for line in line_make():
    print(line)