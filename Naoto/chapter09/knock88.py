'''
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
'''


import pickle
import scipy.io as sio
from numpy.linalg import norm


def load(file_name):
    with open(f"./pickles/{file_name}.pkl", "rb") as f_in:
        data = pickle.load(f_in)
    return data


def cos_sim(a, b):
    return a @ b / norm(a) / norm(b)


top10 = []
ft = load('ft')
t2i = {token: i for i, token in enumerate(ft)}
i2t = {i: token for i, token in enumerate(ft)}
X_300 = sio.loadmat("./pickles/X_300.mat")["X_300"]
for i, word in enumerate(X_300):
    # if i != t2i["England"]:
    sim = cos_sim(word, X_300[t2i["England"]])
    top10.append([sim, i])
    top10.sort(key=lambda x: x[0], reverse=True)
    top10 = top10[0:10]

for sim, i in top10:
    print(i2t[i], sim)
