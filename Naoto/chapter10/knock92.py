'''
92. アナロジーデータへの適用
91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
'''


import pickle
import scipy.io as sio
import word2vec
import numpy as np


def load(file_name):
    with open(f"../chapter09/pickles/{file_name}.pkl", "rb") as f_in:
        data = pickle.load(f_in)
    return data


def cos_sim(a, b):
    dot = np.dot(a, b)
    if dot == 0:
        return -1
    return dot / np.linalg.norm(a) / np.linalg.norm(b)


ft = load('ft')
t2i = {token: i for i, token in enumerate(ft)}
X_300 = sio.loadmat("../chapter09/pickles/X_300.mat")["X_300"]

in_file = "out91.txt"
out_file_85 = "out92_85.txt"
out_file_90 = "out92_90.txt"

max_sim = 0
max_token = 0
with open(out_file_85, "w") as f_out:
    for line in map(lambda x: x.rstrip(), open(in_file)):
        words = line.split()
        v = X_300[t2i[words[1]]] - X_300[t2i[words[0]]] + X_300[t2i[words[2]]]
        for token in ft:
            sim = cos_sim(X_300[t2i[token]], v)
            if sim > max_sim:
                max_sim = sim
                max_token = token
        f_out.write(line + " " + max_token + "\n")
