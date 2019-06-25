'''
889. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，
vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''
import pickle
import scipy.io as sio
import numpy as np
from scipy import sparse


def load(file_name):
    with open(f"./pickles/{file_name}.pkl", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


def cos_sim(a, b):
    dot = np.dot(a, b)
    if dot == 0:
        return -1
    return np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)


ft = load('ft')
t2i = {token: i for i, token in enumerate(ft)}
vec = sio.loadmat('./pickles/X_300.mat')['X_300']

tgt = vec[t2i["Spain"]] - vec[t2i["Madrid"]] + vec[t2i["Athens"]]

ranking = {key: cos_sim(vec[t2i[key]], tgt) for key in ft}
for key, val in sorted(ranking.items(), key=lambda x: -x[1])[:10]:
    print(key, val)


''' result
Sweden 0.854315487629981
Spain 0.8496053499118794
Austria 0.8483267727230223
Italy 0.8112847621420561
Netherlands 0.8089279994456934
Germany 0.8083536675903666
Belgium 0.7828949566341542
Denmark 0.7825201667436116
Télévisions 0.7786531471544621
Norway 0.7732616259359913
'''
