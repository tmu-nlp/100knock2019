'''
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，
"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
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
X_300 = sio.loadmat('./pickles/X_300.mat')['X_300']

v = X_300[t2i['England']]
ranking = {key: cos_sim(X_300[t2i[key]], v) for key in ft}
for key, val in sorted(ranking.items(), key=lambda x: -x[1])[:10]:
    print(key, val)


'''
England 1.0000000000000004
Scotland 0.6086578653930685
Australia 0.6058383924870612
Italy 0.5927295912332593
Wales 0.592102550219518
France 0.5827301759366093
Germany 0.5544064015304
Spain 0.5409634949594645
Japan 0.5088001406586814
Cheshire 0.4901537711713514
'''
