'''
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
'''
import pickle
import scipy.io as sio
from numpy.linalg import norm
from scipy import sparse


def load(file_name):
    with open(f"./pickles/{file_name}.pkl", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


def cos_sim(a, b):
    return a @ b / norm(a) / norm(b)


ft = load('ft')
t2i = {token: i for i, token in enumerate(ft)}
X_300 = sio.loadmat('./pickles/X_300.mat')['X_300']

a = X_300[t2i['United_States']]     # `United States`
b = X_300[t2i['U.S']]               # `U.S.`
print(cos_sim(a, b))                # 0.8147650884663092
