"""
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
"""

import pickle, json
import sys, pathlib
import numpy as np

sys.path.append(str(pathlib.Path() / ".." / "chapter08"))

from knock72 import serialize, deserialize


def main():
    # word2vec のすべてのベクトルを読み込む
    matrix, t_index = deserialize("matrix"), deserialize("t_index")

    # 国名のリストの読み込み
    with open("../data/country.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    countries = [d["name"] for d in data]

    new_matrix, new_index = [], {}
    for c in countries:
        if not c in t_index:
            continue
        new_matrix.append(matrix[t_index[c]])
        new_index[c] = t_index[c]

    serialize("country.matrix", new_matrix)
    serialize("country.index", new_index)


if __name__ == "__main__":
    main()
