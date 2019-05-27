class Morph:
    # コンストラクタ
    # surface(表層形), base(基本形), pos(品詞), pos1(品詞細分類1)
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    # __str__ オブジェクトを文字列にして返す
    def __str__(self):
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.format(self.surface, self.base, self.pos, self.pos1)


def make_list(filename: str):
    neko_list = []  # 1文ごとの解析結果が配列として格納
    with open(filename, 'r') as f:
        # 1単語ごとの解析結果が格納
        # surface[　]     base[　]        pos[記号]       pos1[空白]
        str_list = []
        for line in f:
            # 'EOS'を文末と判断してneko_listにstr_listを格納
            if line == 'EOS\n':
                neko_list.append(str_list)
                str_list = []
            else:
                # 1文字目が'*'の場合、文節情報のためここでは飛ばす
                # * 0 2D 0/0 -0.764522
                if line[0] == '*':
                    continue

                # line = 吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ,,
                line = line.split('\t')
                cal1 = line[0]
                cal2 = line[1].split(',')
                str_list.append(Morph(cal1, cal2[6], cal2[0], cal2[1]))

    return neko_list


def main():
    neko_list = make_list('neko.txt.cabocha')
    for m in neko_list[2]:
        print(m)


if __name__ == "__main__":
    main()
