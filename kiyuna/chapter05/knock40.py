'''
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），
品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
'''
import pprint
from itertools import islice
from collections import namedtuple

Morph = namedtuple('Morph', ('surface', 'base', 'pos', 'pos1'))


def cabocha_into_morphs(f_name='neko.txt.cabocha'):
    sentence = []
    with open(f_name) as f:
        for line in map(lambda x: x.rstrip(), f):
            if line == "EOS":
                yield sentence
                sentence = []
            else:
                if line[0] == '*':
                    continue
                surface, details = line.split('\t')
                mecab_keys = ["品詞", "品詞細分類1", "品詞細分類2", "品詞細分類3",
                              "活用型", "活用形", "原形", "読み", "発音"]
                d = dict(zip(mecab_keys, details.split(',')))
                sentence.append(
                    Morph(
                        surface=surface,
                        base=d["原形"],
                        pos=d["品詞"],
                        pos1=d["品詞細分類1"],
                    )
                )


if __name__ == "__main__":
    for morphs in islice(cabocha_into_morphs(), 3, 4):
        pprint.pprint(morphs)


''' NOTE
* mecab と同じ出力フォーマット
    - 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
'''
