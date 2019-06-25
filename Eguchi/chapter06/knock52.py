#51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． 
# Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

from nltk import stem
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


def stem_make():
    stemmer = stem.PorterStemmer()
    for word in word_make():
        yield word + "\t" + stemmer.stem(word)

for word in stem_make():
    print(word)

