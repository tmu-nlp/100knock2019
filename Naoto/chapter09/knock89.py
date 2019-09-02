'''
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''


import pickle
import scipy.io as sio
import numpy as np


def load(file_name):
    with open(f"./pickles/{file_name}.pkl", "rb") as f_in:
        data = pickle.load(f_in)
    return data


def cos_sim(a, b):
    dot = np.dot(a, b)
    if dot == 0:
        return -1
    return dot / np.linalg.norm(a) / np.linalg.norm(b)


ft = load('ft')
t2i = {token: i for i, token in enumerate(ft)}
X_300 = sio.loadmat("./pickles/X_300.mat")["X_300"]
vec = X_300[t2i["Spain"]] - X_300[t2i["Madrid"]] + X_300[t2i["Athens"]]
ranking = {key: cos_sim(X_300[t2i[key]], vec) for key in ft}
for key, val in sorted(ranking.items(), key=lambda x: -x[1])[:10]:
    print(key, val)
