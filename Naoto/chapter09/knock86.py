'''
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
'''

import pickle
import scipy.io as sio
from scipy import sparse


def dump(file_name, data):
    with open(f"./pickles/{file_name}.pkl", 'wb') as f_out:
        pickle.dump(data, f_out)


def load(file_name):
    with open(f"./pickles/{file_name}.pkl", "rb") as f_in:
        data = pickle.load(f_in)
    return data


ft = load('ft')
t2i = {token: i for i, token in enumerate(ft)}
X_300 = sio.loadmat('./pickles/X_300.mat')['X_300']
X_lil = sparse.lil_matrix(X_300)

print(X_lil[t2i['United_States']])
print(X_300[t2i['United_States']])
