'''
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．

- f(t,c) ≥ 10ならば，Xtc = PPMI(t,c) = max{log N×f(t,c) / f(t,*)×f(*,c), 0}
- f(t,c) < 10ならば，Xtc = 0

ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる
統計量である．なお，行列Xの行数・列数は数百万オーダとなり，
行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
'''
import pickle
from math import log


def dump(file_name, data):
    with open(f"./pickles/{file_name}.pkl", 'wb') as f_out:
        pickle.dump(data, f_out)


def load(file_name):
    with open(f"./pickles/{file_name}.pkl", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


f = load('f')
ft = load('ft')
fc = load('fc')
N = load('N')

X = {}
for (t, c), f_tc in f.items():
    if f_tc < 10:
        continue
    X[t, c] = max(log(N * f_tc / ft[t] / fc[c]), 0)

dump('X', X)
