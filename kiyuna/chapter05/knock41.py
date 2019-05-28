'''
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
'''
import pprint
from itertools import islice
from collections import namedtuple, defaultdict
from typing import Dict

Morph = namedtuple('Morph', 'surface, base, pos, pos1')


class Chunk:
    def __init__(self, morphs=[], dst=None, srcs=[]):
        self.morphs, self.dst, self.srcs = morphs[:], dst, srcs[:]

    def __repr__(self):
        clause = ''.join(m.surface for m in self.morphs)
        return f'Chunk(srcs={self.srcs}, dst={self.dst}, morphs={clause})'

    def __getitem__(self, key):
        if key == 0:
            return self.morphs
        elif key == 1:
            return self.dst
        elif key == 2:
            return self.srcs
        else:
            raise IndexError


def cabocha_into_chunks(f_name: str='neko.txt.cabocha') -> Dict[int, Chunk]:
    chunks = defaultdict(Chunk)
    with open(f_name) as f:
        for line in map(lambda x: x.rstrip(), f):
            if line == "EOS":
                yield {k: v for k, v in sorted(chunks.items()) if k >= 0}
                chunks.clear()
            elif line[0] == '*':
                _, idx, dst, *_ = line.split()
                idx = int(idx)
                dst = int(dst[:-1])
                chunks[idx].dst = dst
                chunks[dst].srcs.append(idx)
            else:
                surface, details = line.split('\t')
                mecab_keys = ["品詞", "品詞細分類1", "品詞細分類2", "品詞細分類3",
                              "活用型", "活用形", "原形", "読み", "発音"]
                d = dict(zip(mecab_keys, details.split(',')))
                chunks[idx].morphs.append(
                    Morph(
                        surface=surface,
                        base=d["原形"],
                        pos=d["品詞"],
                        pos1=d["品詞細分類1"],
                    )
                )
    raise StopIteration


if __name__ == "__main__":
    for chunks in islice(cabocha_into_chunks(), 7, 8):
        pprint.pprint(chunks)


''' NOTE
* CaboChaによる係り受け解析結果は，形態素解析結果の前に挿入される `*` から始まる行
- https://taku910.github.io/cabocha/
    - * 1 2D 0/1 -0.764522          <- この行が文節の開始位置を意味している
        │ │   │   └─係り関係のスコア:
        │ │   │       係りやすさの度合を示します. 一般に大きな値ほど係りやすいことを表す
        │ │   └─ 主辞/機能語の位置
        │ └─ 係り先番号
        └─ 文節番号（0から始まる整数）
'''
