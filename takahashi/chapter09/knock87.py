"""
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
"""

import sys
import numpy as np
import redis, pickle
from scipy.io import loadmat
from collections import OrderedDict



# 欠損値 (nan) を無視して、cos 類似度が nan にならないように求める
def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> np.float64:
    # マスクした値を無視して norm を求める
    v1_norm = np.sqrt(np.nansum(v1 ** 2))
    v2_norm = np.sqrt(np.nansum(v2 ** 2))

    # 内積を求めるためにマスクした値を無視して、要素ごとの積を求める
    dot = np.nansum(v1 * v2)

    # nan を無視しているので norm が 0 になる場合に -1 を割り当てる
    norm = v1_norm * v2_norm
    if norm == 0:
        return -1
    res = dot / (v1_norm * v2_norm)
    return res


def main():
    r = redis.Redis(host="localhost", port=6379, db=0)
    matrix = loadmat("knock85.matrix")["knock85.matrix"]
    t = pickle.loads(r.get("knock83.t"))

    t_index = OrderedDict((key, i) for i, key in enumerate(t.keys()))

    u_s = matrix[t_index["United_States"]]
    us = matrix[t_index["U.S"]]

    print(cosine_similarity(u_s, us))


if __name__ == "__main__":
    main()

"""
実行結果
0.8349214932941352

"""
