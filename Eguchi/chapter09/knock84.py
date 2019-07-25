"""
83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．
f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
f(t,c)<10ならば，Xtc=0
"""
import math
import pickle
from scipy import sparse, io
from collections import Counter
from collections import OrderedDict

N=71249957
tc_count_fname = r"tc_counter"
t_count_fname = r"t_counter"
c_count_fname = r"c_counter"
fname_matrix_x = r'matrix_x'
fname_dict_index_t = r'dict_index_t'

with open(tc_count_fname, "rb") as f:
    tc_counter = pickle.load(f)
with open(t_count_fname, "rb") as f:
    t_counter = pickle.load(f)
with open(c_count_fname, "rb") as f:
    c_counter = pickle.load(f)

dict_index_t = OrderedDict((key, i) for i, key in enumerate(t_counter.keys()))
dict_index_c = OrderedDict((key, i) for i, key in enumerate(c_counter.keys()))

t_size = len(dict_index_t)

c_size = len(dict_index_c)
matrix_x = sparse.lil_matrix((t_size, c_size))

for i, (k, v) in enumerate( tc_counter.items()):
    if v >= 10:
        keys = k.split("\t")        
        t = keys[0]
        c = keys[1]
        ppmi = max(math.log(N * v /t_counter[t] / c_counter[c] ), 0 )
        matrix_x[dict_index_t[t], dict_index_c[c]] = ppmi
    
    if i % 100000 == 0:
        print('{} done.'.format(i))

io.savemat(fname_matrix_x, {'matrix_x': matrix_x})
with open(fname_dict_index_t, 'wb') as data_file:
    pickle.dump(dict_index_t, data_file)
