# 49. 名詞間の係り受けパスの抽出
# 文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
# ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
#  - 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
#  - 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する

# また，係り受けパスの形状は，以下の2通りが考えられる．
#  - 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
#  - 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
#    文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，
#    文節kの内容を"|"で連結して表示

from knock41 import load_chunk_cabocha, Chunk
from itertools import combinations
from collections import defaultdict
from typing import List, Dict

# path dictionary
PD = Dict[int, List[int]]


def join_phrase(i: int, j: int, phrase_path: PD, chunks: Chunk) -> str:
    result = chunks[i].masked_noun("X")
    if j in phrase_path[i]:
        result += " -> "
        # 文節 i から構文木の根に至る経路上に文節 j が存在する場合
        for path in phrase_path[i]:
            if path == j:
                result += "Y"
                break
            else:
                result += chunks[path].no_symbols() + " -> "
    else:
        # 文節 i と文節 j から構文木の根に至る経路上で共通の文節 k で交わる場合
        for path in phrase_path[i]:
            if path not in phrase_path[j]:
                # 文節 k に未到達
                result += " -> " + chunks[path].no_symbols()
                continue

            # 文節 k に到達
            # Y を追加し、文節 j から根に至る (或いは共通の文節) まで探索
            result += " | " + chunks[j].masked_noun("Y")
            for p in phrase_path[j]:
                if path != p:
                    result += " -> " + chunks[p].no_symbols()
                    continue
                result += " | " + chunks[path].no_symbols()
                return result
    return result


def get_dependency_path_between_nouns() -> None:
    for chunks in load_chunk_cabocha():
        phrase_path = defaultdict(list)  # type: PD
        for i, chunk in enumerate(chunks):
            if not any(m.pos == "名詞" for m in chunk.morphs):
                continue
            if chunk.dst == -1:
                phrase_path[i] = []
                continue
            current = chunk
            while current.dst != -1:
                phrase_path[i].append(current.dst)
                current = chunks[current.dst]

        for i, j in combinations(phrase_path.keys(), 2):
            print(join_phrase(i, j, phrase_path, chunks))


if __name__ == "__main__":
    get_dependency_path_between_nouns()

"""
実行結果

Xは -> Y
Xで -> 生れたか | Yが | つかぬ
Xでも -> 薄暗い -> Y
Xでも -> 薄暗い -> 所で | Y | 泣いて
Xでも -> 薄暗い -> 所で -> 泣いて | Yだけは | 記憶している
Xでも -> 薄暗い -> 所で -> 泣いて -> Y
Xで | Y | 泣いて
Xで -> 泣いて | Yだけは | 記憶している
Xで -> 泣いて -> Y
X -> 泣いて | Yだけは | 記憶している
X -> 泣いて -> Y
Xだけは -> Y
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
...

"""
