##形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），
# 品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
# 各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．


import CaboCha
import re
class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

path = r"\Users\Koya\Documents\Lab\neko.txt.cabocha"
with open(path,mode = "r" ,encoding= "utf-8") as cabochaf:
    splitedlines =cabochaf.read() 
    

eachlist = []
alllist = []
for line in splitedlines.split("\n"):
    temp = line.split("\t")
    if len(temp) >= 2:
        splittemp = temp[1].split(",")
        if not splittemp[1] == "空白":
            eachlist.append(Morph(temp[0],splittemp[6],splittemp[0],splittemp[1]))
    elif temp[0] == "EOS":
        alllist.append(eachlist)
        eachlist = []


for item in alllist[5]:
    print ('surface=%s\tbase=%s\tpos=%s\tpos1=%s' % (item.surface, item.base, item.pos, item.pos1) )

