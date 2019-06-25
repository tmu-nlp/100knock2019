# 85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
# そのベクトルと類似度の高い10語とその類似度を出力せよ．

import pickle
import numpy as np
from collections import defaultdict


def save(file_name, data):
    with open(f"./pickles/{file_name}", 'wb') as f_out:
        pickle.dump(data, f_out)


def load(file_name):
    with open(f"./pickles/{file_name}", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


if __name__ == "__main__":
    # import X (300dimension) and t
    X300 = load('X300')
    t = load('t')

    # set PCA with num of principal components = 300
    pca = PCA(n_components=300)

    # execute PCA
    X300 = pca.fit_transform(X)

    v1 = X300[t['England']]
    v2 = X300[t['Madrid']]
    v3 = X300[t['Athens']]

    v_ref = v1 - v2 + v3

    vectors = default
    for key in t:
        v = X300[t[key]]
        cosin[key] = np.dot(v, v_ref)

    i = 0
    for key, val in sorted(cosin.items(), reverse=True)
        if i>10:
            break
        print(key, val)
    