# 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラスChunkを実装せよ．
# このクラスは形態素（Morphオブジェクト）のリスト（morphs），
# 係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
# さらに，入力テキストのCaboChaの解析結果を読み込み，
# １文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．

from typing import List, Dict
from knock40 import Morph
from collections import defaultdict
import re


class Chunk:
    def __init__(self, morphs, dst, srcs) -> None:
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def __repr__(self) -> str:
        chunk = "".join([morph.surface for morph in self.morphs])
        return f"{chunk} {self.dst}"

    def no_symbols(self) -> str:
        """ 記号を除いた表層形で文字列を返す """
        chunk = "".join([m.surface for m in self.morphs if m.pos != "記号"])
        return chunk

    def masked_noun(self, mask: str) -> str:
        """
        名詞を文字列 mask で置換する
        名詞が複数含まれていた場合に、すでにマスクされていれば名詞を置換しない
        """
        noun = ""
        is_masked = False
        for m in self.morphs:
            if is_masked:
                if m.pos != "記号":
                    noun += m.surface
            else:
                if m.pos == "名詞":
                    noun += mask
                    is_masked = True
                elif m.pos != "記号":
                    noun += m.surface
        return noun


C = List[Chunk]
T = List[C]


def load_chunk_cabocha(file="./data/neko.txt.cabocha") -> T:
    results = []  # type: T
    chunks = []  # type: C
    current = -1  # 現在参照している文節番号
    srcs = {}  # type: Dict[int, List[int]] # key: 文節番号, value: 文節に係る元の文節番号

    for line in open(file, encoding="utf-8"):
        line = line.rstrip("\n")
        # 行頭が * で始まる行
        if line.startswith("*"):
            current += 1
            elem = line.split(" ")
            dst = int(elem[2][:-1])
            # 文節のリストに文節を追加する
            chunks.append(Chunk([], dst, []))
            if dst != -1:
                if dst in srcs:
                    srcs[dst].append(int(elem[1]))
                else:
                    srcs[dst] = [int(elem[1])]
        # EOS
        elif line == "EOS":
            if chunks == []:
                continue
            for key, value in srcs.items():
                chunks[key].srcs = value
            results.append(chunks)
            # 初期化
            chunks, current, srcs = [], -1, {}
        else:
            splitted = re.split("[\t,]", line)
            chunks[current].morphs.append(Morph(splitted[0], splitted[7], splitted[1], splitted[2]))

    return results


if __name__ == "__main__":
    for i, s in enumerate(load_chunk_cabocha()[7]):
        print(f"{i:>2} : {s}")

"""
実行結果

 0 : この 1
 1 : 書生というのは 7
 2 : 時々 4
 3 : 我々を 4
 4 : 捕えて 5
 5 : 煮て 6
 6 : 食うという 7
 7 : 話である。 -1

"""
