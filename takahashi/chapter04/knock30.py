# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
# キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．

from typing import List,Dict
import re

M = List[Dict[str, str]]
T = List[M]

def load_morpheme(file="neko.txt.mecab") -> T:
    morphemes = [] # type: T
    sentence = []  # type: M
    for line in open(file, encoding="utf-8"):
        line = line.rstrip("\n")
        elements = re.split("[\t,]", line)
        if elements[0] == "EOS":
            if sentence == []:
                continue
            morphemes.append(sentence)
            sentence = []
        else:
            morpheme = {
                "surface": elements[0],
                "base"   : elements[7],
                "pos"    : elements[1],
                "pos1"   : elements[2]
            }
            sentence.append(morpheme)
    return morphemes

def load_morpheme_list(file="neko.txt.mecab") -> M:
    morphemes = [] # type: M
    for line in open(file, encoding="utf-8"):
        line = line.rstrip("\n")
        elements = re.split("[\t,]", line)
        if elements[0] == "EOS":
            continue
        else:
            morpheme = {
                "surface": elements[0],
                "base"   : elements[7],
                "pos"    : elements[1],
                "pos1"   : elements[2]
            }
            morphemes.append(morpheme)
    return morphemes
        

if __name__ == "__main__":
    for sentence in load_morpheme():
        for morpheme in sentence:
            print(morpheme)

# mecab 出力フォーマット
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音