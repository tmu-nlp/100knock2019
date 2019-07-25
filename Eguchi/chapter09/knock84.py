"""
83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．
f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
f(t,c)<10ならば，Xtc=0
"""
import math
import pickle

N=71249957
tc_count_fname = r"tc_counter"
t_count_fname = r"t_counter"
c_count_fname = r"c_counter"

with open(tc_count_fname, "rb") as f:
    tc_counter = pickle.load(f)
with open(t_count_fname, "rb") as f:
    t_counter = pickle.load(f)
with open(c_count_fname, "rb") as f:
    c_counter = pickle.load(f)
print("tc_counter\n")
i=0
for k, v in tc_counter.items():
    print("k={} v={}" .format(k,v))
    i+=1
    if i >100:
        break
print("t_counter\n")
i=0
for k, v in t_counter.items():
    print("k={} v={}" .format(k,v))
    i+=1
    if i >100:
        break

print("c_counter\n")
i=0
for k, v in c_counter.items():
    print("k={} v={}" .format(k,v))
    i+=1
    if i >100:
        break

"""
if tc_counter >= 10:
    X = max(math.log(N * tc_counter /  ))
"""