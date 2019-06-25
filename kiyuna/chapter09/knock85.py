'''
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
'''
import pickle
import scipy.io as sio
from scipy import sparse
from sklearn.decomposition import TruncatedSVD


def dump(file_name, data):
    with open(f"./pickles/{file_name}.pkl", 'wb') as f_out:
        pickle.dump(data, f_out)


def load(file_name):
    with open(f"./pickles/{file_name}.pkl", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


X = load('X')
ft = load('ft')
fc = load('fc')
t2i = {token: i for i, token in enumerate(ft)}
c2i = {token: i for i, token in enumerate(fc)}
X_idxed = {(t2i[t], c2i[c]): v for (t, c), v in X.items()}
X_s = sparse.dok_matrix((len(ft), len(fc)))
X_s.update(X_idxed)
pca = TruncatedSVD(n_components=300)
X_300 = pca.fit_transform(X_s)

sio.savemat('./pickles/X_300.mat', {'X_300': X_300})


'''
* scipy.sparse.dok_matrix
https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.dok_matrix.html

* scipy.io
https://docs.scipy.org/doc/scipy/reference/tutorial/io.html

* scipy.sparse の内部データ構造
http://hamukazu.com/2014/12/03/internal-data-structure-scipy-sparse/
'''
