##2つの名詞が「の」で連結されている名詞句を抽出せよ．

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
    NoNoun = []
    for i, line in enumerate(mecabfile):
        if "連体化" in line["pos1"]:
            if ("名詞" in mecabfile[i-1]["pos"]) and ("名詞" in mecabfile[i+1]["pos"]):
                NoNoun.append(mecabfile[i-1]["surface"] + line["surface"] +mecabfile[i+1]["surface"] )
    
    print(NoNoun)



sentence = openmecab()

mecabfile = splitmecab(sentence)

findverb()

"""
書生	ショセイ	書生	名詞-一般		
の	ノ	の	助詞-連体化		
顔	カオ	顔	名詞-一般	
"""