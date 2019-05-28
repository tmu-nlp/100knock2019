'''
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
'''


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f'surface: {self.surface}\tbase: {self.base}\tpos: {self.pos}\tpos1: {self.pos1}'


def get_morpheme_list(file_path: str):
    sentence = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip()

            if line == 'EOS':
                yield sentence
                sentence = []
                continue
            # 係り受け情報は飛ばす
            if line[0] == '*':
                continue

            line = ','.join(line.split("\t")).split(',')

            # Morphクラスをリストに追加
            sentence.append(Morph(
                line[0],  # surface
                line[7],  # base
                line[1],  # pos
                line[2]   # pos1
            ))


if __name__ == '__main__':
    for i, morphs in enumerate(get_morpheme_list("neko.txt.cabocha"), 1):
        if i == 8:
            for morph in morphs:
                print(morph)
            break

# cabocha -f1 < neko.txt > neko.txt.cabocha
