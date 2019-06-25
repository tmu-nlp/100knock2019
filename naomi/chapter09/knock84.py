# 83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．

# f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
# f(t,c)<10ならば，Xtc=0
# ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
# なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．
# 幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．

from tqdm import tqdm
from collections import defaultdict
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
    # Import dictionaries
    t_count = load('t')
    c_count = load('c')
    tc_count = load('tc')
    N = load('N')

    xtc = defaultdict(float)
    for tc, counts in tqdm(tc_count.items()):
        t, c = tc.split()
        if counts < 10:
            continue
        else:
            xtc = max([0, np.log2(N*counts/(t_count[t]*c_count[c]))])
    save('Xtc', xtc)