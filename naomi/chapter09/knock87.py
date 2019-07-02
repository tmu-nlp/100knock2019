# 85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
# ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．

import pickle
import numpy as np


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

    v1 = X300[t['United_States']]
    v2 = X300[t['U.S']]

    print(np.dot(v1, v2))
    