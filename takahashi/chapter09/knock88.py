"""
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．

"""


import numpy as np
import redis, pickle
from collections import OrderedDict
from operator import itemgetter
from scipy.io import loadmat
from knock87 import cosine_similarity


def main():
    r = redis.Redis(host="localhost", port=6379, db=0)
    matrix = loadmat("knock85.matrix")["knock85.matrix"]
    t = pickle.loads(r.get("knock83.t"))

    t_keys = list(t.keys())
    t_index = OrderedDict((key, i) for i, key in enumerate(t_keys))

    eng = matrix[t_index["England"]]
    dist = {t_keys[i]: cosine_similarity(eng, matrix[i]) for i in range(len(t_index))}
    rank = sorted(dist.items(), key=itemgetter(1), reverse=True)

    for i in range(1, 11):
        print(f"{rank[i][0]}\t{rank[i][1]}")


if __name__ == "__main__":
    main()


"""
実行結果
Scotland	0.6313365754660833
Australia	0.6023631275796418
Wales	0.571680812410387
France	0.5566636831991816
Ireland	0.5447797976144033
Japan	0.5347015539301986
Spain	0.5235723848572322
Italy	0.5163037528367883
Germany	0.5049634623867687
United_Kingdom	0.5005813957305484

"""
