##形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

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


sentence = openmecab()
splitmecab(sentence)



"""
['た', 'タ', 'た', '助動詞', '特殊・タ', '基本形']
['が', 'ガ', 'が', '助詞-接続助詞', '', '']
['、', '、', '、', '記号-読点', '', '']
['やがて', 'ヤガテ', 'やがて', '副詞-一般', '', '']
['そん', 'ソン', 'そん', '名詞-一般', '', '']
['なら', 'ナラ', 'だ', '助動詞', '特殊・ダ', '仮定形']
"""