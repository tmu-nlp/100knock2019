'''
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），\
    品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）\
    を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
'''


import re


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def cabocha_Morph_read() -> []:
    '''
    １文ごとに形態素のリストを返す
    '''
    path = 'neko.txt.cabocha'
    morph_list = []
    for line in open(path):
        line_list = re.split("[\t,]", line.rstrip())
        if line_list[0] != "*" and len(line_list) > 1:
            morph = Morph(line_list[0], line_list[6], line_list[1], line_list[2])
            morph_list.append(morph)
        elif line_list[0] == "EOS":
            if len(morph_list) > 0:
                yield morph_list
                morph_list = []


def main():
    for i, morphs in enumerate(cabocha_Morph_read()):
        if i < 2:
            continue
        for morph in morphs:
            print(morph.surface, morph.base, morph.pos, morph.pos1)
        break


if __name__ == '__main__':
    main()


''' 実行結果
名前 * 名詞 一般
は * 助詞 係助詞
まだ * 副詞 助詞類接続
無い 基本形 形容詞 自立
。 * 記号 句点
'''
