"""
82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
"""
from collections import Counter
import pickle

in_name = "outpu82.100.txt"
tc_count_fname = r"tc_counter"
t_count_fname = r"t_counter"
c_count_fname = r"c_counter"



tc_counter = Counter()
t_counter = Counter()
c_counter = Counter()

tc_temp = list()
t_temp = list()
c_temp = list()


with open(in_name, "rt", encoding="utf-8") as in_f:
    for i, line in enumerate(in_f):
        line = line.strip()
        words = line.split("\t")
        
        tc_temp.append(line)
        t_temp.append(words[0])
        c_temp.append(words[1])

        if i % 1000000 == 0:
            tc_counter.update(tc_temp)
            t_counter.update(t_temp)
            c_counter.update(c_temp)
            tc_temp = []
            t_temp = []
            c_temp = []
            print('{} done.'.format(i))
    
    tc_counter.update(tc_temp)
    t_counter.update(t_temp)
    c_counter.update(c_temp)

with open(tc_count_fname, "wb") as f:
    pickle.dump(tc_counter, f)
with open(t_count_fname, "wb") as f:
    pickle.dump(t_counter, f)
with open(c_count_fname, "wb") as f:
    pickle.dump(c_counter, f)

print('N={}'.format(i))