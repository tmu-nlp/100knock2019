#空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

import re
path = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt"

def line_make():
    linelist = []
    with open(path,mode = "r",encoding='utf-8' ) as f:
        for line in f:
            line = re.sub(r"(?P<group>[.:;!?])(\s)(?P<group3>[A-Z])", r"\1\n\3", line )
            linelist.append(line)

    return linelist

def word_make():
    for line in line_make():
        for word in line.split(" "):
            yield word
        yield ""

for word in word_make():
    print(word)




