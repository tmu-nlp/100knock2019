# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は
# 表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

# １文ずつ読み込む形にしたほうがわかりよい


def importmecab(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as f:

        # 文のリストを格納するリスト
        sentences = []
        # １文に含まれる形態素のタプルを格納するリスト
        sentence = []

        for line in f:
            # １行をコラムごとに分割
            cols = line.rstrip().split(',')

            if cols[0] == 'EOS':
                sentences.append(sentence)
                sentence = []
                continue

            # １列目は'形態素   品詞'
            words = cols[0].split('\t')

            morphs = {
                'surface': words[0],
                'base': cols[6],
                'pos': words[1],
                'pos1': cols[1]
            }

            # 文のリストにタプルを追加
            sentence.append(morphs)

        return sentences


def main():
    path = 'neko.txt.mecab'

    importmecab(path)


if __name__ == '__main__':
    main()
