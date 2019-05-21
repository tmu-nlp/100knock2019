'''
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''
from typing import List


def get_morpheme_list(file_path: str) -> List[dict]:
    sentence = []
    morpheme = {}
    with open(file_path) as f:
        for line in f:
            line = line.rstrip()
            if line != 'EOS':
                # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
                line = ','.join(line.split('\t')).split(',')

                morpheme = {'surface': line[0], 'base': line[7],
                            'pos': line[1], 'pos1': line[2]}

                sentence.append(morpheme)

                if line[2] == '句点':
                    yield sentence
                    sentence = []


if __name__ == '__main__':
    for sentence in get_morpheme_list('neko.txt.mecab'):
        print(sentence)

# mecab neko.txt -o neko.txt.mecab