import re
from typing import List
from collections import defaultdict

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return "surface: '{}', base: '{}', pos: '{}', pos1: '{}'".format(self.surface, self.base, self.pos, self.pos1)

class Chunk:
    def __init__(self, index, morphs, dst, srcs):
        self.index = index
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
        self.morphstr = "".join(list(map(lambda x: x.surface, self.morphs)))

    def __repr__(self):
        return "\n[{}] morphs: {}, dst: {}, srcs: {}".format(self.index, self.morphstr, self.dst, self.srcs)


def load_chunk_list(file_name: str, max_len: int = 100) -> List[List[dict]]:
    # 入力
    # 期待する出力
    '''
    [0] morphs:  , dst: 2, srcs: [], 
    [1] morphs: 吾輩は, dst: 2, srcs: [], 
    [2] morphs: 猫である。, dst: -1, srcs: [0, 1]
    '''
    with open(file_name, encoding="utf8") as f:
        sentence_list = []
        chunk_list = []
        chunk_list_cal_srcs = []
        morph_list = []
        index = 0
        dst = 0
        lines = f.readlines()
        for i in range(len(lines))[:max_len]:
            line = lines[i]

            # 解析結果の表示
            if line[0] == "*":
                if morph_list != []:
                    # srcsは文全体の文節を見ないといけないので、あとで計算する
                    chunk = [morph_list, dst, index]
                    chunk_list_cal_srcs.append(chunk)
                    morph_list = []
                '''
                ex. * 1 2D 0/1 -0.764522
                1. *
                2. 文節番号
                3. 係り先の文節番号(係り先なし:-1)
                4. 主辞の形態素番号/機能語の形態素番号
                5. 係り関係のスコア(大きい方が係りやすい)
                '''
                split = line.split()
                index = int(split[1])
                dst = int(split[2].strip("D"))
                continue

            # EOS1つ: 文の区切り
            # EOS2つ: 文章の区切り
            if line == "EOS\n":
                if lines[i-1] == "EOS\n":
                    continue
                if morph_list != []:
                    chunk = [morph_list, dst, index]
                    chunk_list_cal_srcs.append(chunk)
                    morph_list = []
                # srcsの計算結果を入れるlist
                srcs = [[] for _ in chunk_list_cal_srcs]
                
                # 文の終わりなら文節のリストを入れる
                for chunk in chunk_list_cal_srcs:
                    if chunk[1] != -1:
                        # 各chunkから、srcsを求める
                        srcs[chunk[1]].append(chunk[2])
                for chunk in chunk_list_cal_srcs:
                    # index, morphs, dst, srcsをchunkのlistに入れる
                    chunk_list.append(Chunk(chunk[2], chunk[0], chunk[1], srcs[chunk[2]]))
                sentence_list.append(chunk_list)
                chunk_list = []
                chunk_list_cal_srcs = []
                continue

            splited = re.split("[\t,]", line)

            morph = Morph(splited[0], splited[7], splited[1], splited[2])
            morph_list.append(morph)
    return sentence_list

if __name__ == "__main__":
    sentence_list = load_chunk_list("neko.txt.cabocha")
    for sentence in sentence_list[:10]:
        print(sentence)