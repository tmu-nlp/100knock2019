##サ変接続の名詞をすべて抽出せよ．



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
    SaNoun = []
    for line in mecabfile:
        if "名詞" in line["pos"]:
            if "サ変接続" in line["pos1"]:
                SaNoun.append(line["surface"])
    
    print(SaNoun)
    



sentence = openmecab()

mecabfile = splitmecab(sentence)

findverb()
