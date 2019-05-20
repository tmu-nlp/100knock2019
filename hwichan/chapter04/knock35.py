import MeCab
m = MeCab.Tagger()


def make_list(filename: str) -> list:
    neko_list = []  # すべての文が格納
    neko_line = []  # 1文の形態素
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n').split('\t')  # 単語(表層形)と解析結果で分割
            if len(line) > 1:  # EOSは含まない
                cal1 = line[0]
                cal2 = line[1].split(',')
                neko_dict = {'surface': cal1, 'base': cal2[6], 'pos': cal2[0], 'pos1': cal2[1]}

                if neko_dict['pos1'] == '句点':  # '。'が文の終わりと判断
                    neko_line.append(neko_dict)
                    neko_list.append(neko_line)
                    neko_line = []
                else:
                    neko_line.append(neko_dict)

    return neko_list


def main():
    neko_list = make_list('neko.txt.mecab')
    nouns = []
    noun = []
    for line in neko_list:
        for n, word in enumerate(line):
            if word['pos'] == '名詞':
                noun.append(word['surface'])
            else:
                if len(noun) > 1:
                    nouns.append(''.join(noun))
                noun = []

    print(nouns[:10])


if __name__ == '__main__':
    main()

