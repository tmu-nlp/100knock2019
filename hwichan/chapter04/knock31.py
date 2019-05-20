import MeCab
m = MeCab.Tagger()


def make_list(filename: str) -> list:
    neko_list = []
    neko_line = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n').split('\t')
            if len(line) > 1:
                cal1 = line[0]
                cal2 = line[1].split(',')
                neko_dict = {'surface': cal1, 'base': cal2[6], 'pos': cal2[0], 'pos1': cal2[1]}

                if neko_dict['surface'] == '。':
                    neko_line.append(neko_dict)
                    neko_list.append(neko_line)
                    neko_line = []
                else:
                    neko_line.append(neko_dict)

    return neko_list


def main():
    neko_list = make_list('neko.txt.mecab')
    verbs = []
    for line in neko_list:
        for word in line:  # word = {surface, base, pos, pos1}
            if word['pos'] == '動詞':
                verbs.append(word['surface'])

    print(verbs[7])


if __name__ == '__main__':
    main()

