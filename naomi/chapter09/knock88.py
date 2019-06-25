# 85で得た単語の意味ベクトルを読み込み，
# "England"とコサイン類似度が高い10語と，その類似度を出力せよ．

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

    vectors = default
    for key in t:
        v2 = X300[t[key]]
        vectors = np.dot(v1, v2)

    i = 0
    for key, val in sorted(vectors.items())
        if i>10:
            break
        print(key, val)
    