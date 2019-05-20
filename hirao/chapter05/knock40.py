import re
from typing import List
MAX_LEN = 100

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return "surface: '{}', base: '{}', pos: '{}', pos1: '{}'"\
               .format(self.surface, self.base, self.pos, self.pos1)

def load_morph_list(file_name: str) -> List[List[dict]]:
    with open(file_name, encoding="utf8") as f:
        sentence_list = []
        morph_list = []
        # 前の行の値とか使いたいので...
        lines = f.readlines()
        for i in range(len(lines))[:MAX_LEN]:
            line = lines[i]

            # 解析結果の表示
            if line[0] == "*":
                continue

            # EOS1つ: 文の区切り
            # EOS2つ: 文章の区切り
            if line == "EOS\n":
                if lines[i-1] == "EOS\n":
                    continue
                # 文の終わりなら形態素のリストを入れる
                sentence_list.append(morph_list)
                morph_list = []
                continue

            splited = re.split("[\t,]", line)
            # 吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイのような形
            morph = Morph(splited[0], splited[7], splited[1], splited[2])
            morph_list.append(morph)
    return sentence_list

if __name__ == "__main__":
    sentence_list = load_morph_list("neko.txt.cabocha")
    for morph in sentence_list[3]:
        print(morph)