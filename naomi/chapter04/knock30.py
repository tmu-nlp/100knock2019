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

            print(words[0], cols[6], words[1], cols[1])
            # 文のリストにタプルを追加
            sentence.append(morphs)

            return sentences


def main():
    path = 'neko.txt.mecab'

    importmecab(path)
    


if __name__ == '__main__':
    main()