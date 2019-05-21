'''
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は
表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとする
マッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
'''
import pprint
from itertools import islice
from typing import List, Dict, Iterator

Morpheme = Dict[str, str]
Sentence = List[Morpheme]


def mecab_into_sentences(f_name: str='neko.txt.mecab') -> Iterator[Sentence]:
    sentence = []
    with open(f_name) as f:
        for line in map(lambda x: x.rstrip(), f):
            if line == "EOS":
                yield sentence
                sentence = []
            else:
                surface, details = line.split('\t')
                mecab_keys = ["品詞", "品詞細分類1", "品詞細分類2", "品詞細分類3",
                              "活用型", "活用形", "原形", "読み", "発音"]
                d = dict(zip(mecab_keys, details.split(',')))
                morpheme = {
                    "surface": surface,
                    "base": d["原形"],
                    "pos": d["品詞"],
                    "pos1": d["品詞細分類1"],
                }
                sentence.append(morpheme)


if __name__ == "__main__":
    for sentence in islice(mecab_into_sentences(), 2, 4):
        pprint.pprint(sentence)


''' NOTE
* mecab の出力フォーマット
    - https://taku910.github.io/mecab/
    - 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
'''
