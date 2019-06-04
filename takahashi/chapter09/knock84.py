"""
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．

  - f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
  - f(t,c)<10ならば，Xtc=0

ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
"""

from collections import OrderedDict
from scipy import sparse as sp
import redis, pickle, pandas
from math import log
from tqdm import tqdm


def main():
    r = redis.Redis(host="localhost", port=6379, db=0)

    tc = pickle.loads(r.get("knock83.tc"))
    t = pickle.loads(r.get("knock83.t"))
    c = pickle.loads(r.get("knock83.c"))
    n = int(r.get("knock83.n"))

    # token/co-word を key とした順序付きの辞書 (value は id)
    t_index = OrderedDict((key, i) for i, key in enumerate(t.keys()))
    c_index = OrderedDict((key, i) for i, key in enumerate(c.keys()))

    # 非 0 要素のみ記憶するのでメモリ節約となる
    sparse_matrix = sp.lil_matrix((len(t_index), len(c_index)))
    for t_c, f_tc in tqdm(tc.items()):
        if f_tc < 10:
            continue

        token, co = t_c.split("\t")
        ppmi = max(log(n * f_tc / t[token] / c[co]), 0)
        sparse_matrix[t_index[token], c_index[co]] = ppmi

    r.set("knock84.t_index", pickle.dumps(t_index, protocol=-1))
    r.set("knock84.c_index", pickle.dumps(c_index, protocol=-1))
    r.set("knock84.sparse_matrix", pickle.dumps(sparse_matrix, protocol=-1))


if __name__ == "__main__":
    main()
