##名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．


import MeCab
import re

def openmecab():
    inputname = r"\Users\Koya\Documents\Lab\neko.txt.mecab"
    with open( inputname, mode = "r",encoding="utf-8")as inputfile:
        splitfile =inputfile.read().split("\n")
        
        return splitfile 
        



def splitmecab(sentence):
    l = []
    for line in sentence:
        if ( r"-" in line):
            line = re.sub("-","\t",line)  ##['吾輩', 'ワガハイ', '吾輩', '名詞-代名詞-一般', '', '']
        l.append(line.split("\t"))
    dictlist =[]
    for i in range(len(l)-2):
        dictwords = {
            "surface": l[i][0],
            "base":l[i][2],
            "pos":l[i][3],
            "pos1":l[i][4]
            }
        dictlist.append(dictwords)
    return dictlist



def findverb():
    LoNoun = []
    for i, line in enumerate(mecabfile):
        if "名詞" in line["pos"] :
            temp = line["surface"]

            for j in range(1,30):
                if "名詞" in mecabfile[i+j]["pos"]:
                    temp = temp  + mecabfile[i+j]["surface"]

                elif not temp == line["surface"]:
                    LoNoun.append(temp)
                    break

                else:
                    break
    
    print(LoNoun)


sentence = openmecab()

mecabfile = splitmecab(sentence)

findverb()