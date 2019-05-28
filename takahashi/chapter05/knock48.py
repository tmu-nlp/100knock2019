# 48. 名詞から根へのパスの抽出
# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
# ただし，構文木上のパスは以下の仕様を満たすものとする．
# - 各文節は（表層形の）形態素列で表現する
# - パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する

from knock41 import load_chunk_cabocha, Chunk
from typing import List


def get_path_from_noun_to_root() -> None:
    for chunks in load_chunk_cabocha():
        for chunk in chunks:
            if chunk.dst == -1:
                continue
            # 文節に名詞が存在しない
            if not any([m.pos == "名詞" for m in chunk.morphs]):
                continue

            dst = chunk.dst
            phrases = [chunk.no_symbols()]
            # 係り先 (Chunk.dst) が -1 になるまで名詞からパスを探索する
            while chunks[dst].dst != -1:
                phrases.append(chunks[dst].no_symbols())
                dst = chunks[dst].dst
            print(" -> ".join(phrases))


if __name__ == "__main__":
    get_path_from_noun_to_root()
