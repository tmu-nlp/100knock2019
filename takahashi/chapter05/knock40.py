# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．
# このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
# さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，
# 3文目の形態素列を表示せよ．

from typing import List
from unicodedata import east_asian_width
import re


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return (
            f"表層形 : {Morph.pp(self.surface, 12)}"
            + f"基本形 : {Morph.pp(self.base, 10)}"
            + f"品詞 : {Morph.pp(self.pos, 10)}"
            + f"品詞細分類1 : {Morph.pp(self.pos1, 10)}"
        )

    # 全角文字を綺麗に表示させる (与えられた文字が半角で何文字分をカウントする)
    @staticmethod
    def pp(string, digit):
        for c in string:
            if east_asian_width(c) in {"F", "W", "A"}:
                digit -= 2
            else:
                digit -= 1
        return string + " " * digit


M = List[Morph]
T = List[M]


def load_morph_cabocha(file="./data/neko.txt.cabocha") -> T:
    # 各文を Morph オブジェクトのリストにして、各文のリストを返す
    morphemes = []  # type: T
    sentence = []  # type: M
    for line in open(file, encoding="utf-8"):
        line = line.rstrip("\n")
        if line == "EOS":
            if sentence == []:
                continue
            morphemes.append(sentence)
            sentence = []
        elif line.startswith("*"):
            continue
        else:
            elem = re.split("[\t,]", line)
            morpheme = Morph(elem[0], elem[7], elem[1], elem[2])
            sentence.append(morpheme)
    return morphemes


if __name__ == "__main__":
    for morph in load_morph_cabocha()[2]:
        print(morph)

"""
実行結果

表層形 : 名前        基本形 : 名前      品詞 : 名詞      品詞細分類1 : 一般
表層形 : は          基本形 : は        品詞 : 助詞      品詞細分類1 : 係助詞
表層形 : まだ        基本形 : まだ      品詞 : 副詞      品詞細分類1 : 助詞類接続
表層形 : 無い        基本形 : 無い      品詞 : 形容詞    品詞細分類1 : 自立
表層形 : 。          基本形 : 。        品詞 : 記号      品詞細分類1 : 句点
"""