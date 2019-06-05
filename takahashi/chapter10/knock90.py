"""
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
"""
import numpy as np
import pickle
from typing import Any, Dict, List, Tuple
from operator import itemgetter
import sys, pathlib

chap08 = pathlib.Path().parent / ".." / "chapter08"
chap09 = pathlib.Path().parent / ".." / "chapter09"
sys.path.extend([str(chap08), str(chap09)])

from knock72 import serialize, deserialize
from knock87 import cosine_similarity

M = List[np.ndarray]
Rank = List[Tuple[str, np.float32]]


def load_word2vec(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        # 先頭に 語彙数,次元数 が記述されている
        vocab_n, dim = f.readline().strip().split()

        t_index = {}  # type: Dict[str, int]
        matrix = []  # type: M
        for i, line in enumerate(f):
            line = line.strip().split()
            t_index[line[0]] = i
            matrix.append(np.array(list(map(np.float32, line[1:]))))

    # 各情報を pickle 化する
    serialize("meta_info", {"vocab_n": vocab_n, "dim": dim})
    serialize("t_index", t_index)
    serialize("matrix", matrix)


def similar_list(mat: M, t_idx: Dict[str, int], v: np.ndarray) -> Rank:
    """ v の類似度が高い n 語とその類似度のリストを返す """
    t_keys = list(t_idx.keys())
    dist = {t_keys[i]: cosine_similarity(v, mat[i]) for i in range(len(t_idx))}
    rank = sorted(dist.items(), key=itemgetter(1), reverse=True)

    return rank


def multi_vec(mat: M, t_idx: Dict[str, int], w1: str, w2: str, w3: str, n=10) -> Rank:
    try:
        v1, v2, v3 = mat[t_idx[w1]], mat[t_idx[w2]], mat[t_idx[w3]]
        vec = v2 - v1 + v3
        return similar_list(mat, t_idx, vec)
    except KeyError:
        return None


def main():
    word2vec_filepath = "../data/w2v.txt"
    load_word2vec(word2vec_filepath)

    matrix, t_index = deserialize("matrix"), deserialize("t_index")

    # knock86
    u_s = matrix[t_index["United_States"]]

    # knock87
    print(cosine_similarity(matrix[t_index["U.S"]], u_s))

    # knock88
    for rank in similar_list(matrix, t_index, matrix[t_index["England"]])[1:11]:
        print(f"{rank[0].ljust(10)} : {rank[1]}")

    # knock89
    for rank in multi_vec(matrix, t_index, "Spain", "Madrid", "Athens")[1:11]:
        print(f"{rank[0].ljust(10)} : {rank[1]}")


if __name__ == "__main__":
    main()


"""
実行結果

-- knock86 --
(省略)

-- knock87 --
0.8529254

-- knock88 --
Scotland   : 0.7456957101821899
Wales      : 0.7315794825553894
Ireland    : 0.6569685339927673
Britain    : 0.5938623547554016
Manchester : 0.5936893224716187
Liverpool  : 0.5615475177764893
London     : 0.5607120990753174
Spain      : 0.5606153011322021
Hampshire  : 0.5600929260253906
Sweden     : 0.5570371150970459

-- knock89 --
Greece     : 0.8113881945610046
Denmark    : 0.8040175437927246
Austria    : 0.7944770455360413
Italy      : 0.7936160564422607
Portugal   : 0.7931720018386841
Russia     : 0.7928892970085144
Athens     : 0.769446849822998
Egypt      : 0.7682836055755615
Romania    : 0.7542145848274231
Bulgaria   : 0.7517447471618652

"""

"""
 - word2vec に適用させる

$ python
>> import word2vec
>> word2vec.word2vec(
    train="../data/knock81.100.txt",  # 81 の出力を入れる
    output="w2v.txt",                 # 出力ファイル名
    size=300,                         # 次元数
    binary=0                          # テキストファイルで保存
)
"""
