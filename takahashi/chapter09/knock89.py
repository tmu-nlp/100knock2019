"""
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．
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

    # スペイン - マドリード (首都) + アテネ (ギリシャの首都)
    vec = (
        matrix[t_index["Spain"]] - matrix[t_index["Madrid"]] + matrix[t_index["Athens"]]
    )
    dist = {t_keys[i]: cosine_similarity(vec, matrix[i]) for i in range(len(t_index))}
    rank = sorted(dist.items(), key=itemgetter(1), reverse=True)

    for i in range(1, 11):
        print(f"{rank[i][0]}\t{rank[i][1]}")


if __name__ == "__main__":
    main()

"""
実行結果

Italy	0.8101239302863255
Austria	0.8064342426453811
Sweden	0.7988784564935523
Germany	0.7927406954619898
Belgium	0.7810113380417819
Netherlands	0.7793133252432883
Denmark	0.766001506308913
Switzerland	0.751374622177831
Télévisions	0.7510455970622103
France	0.7491984403828714
"""
