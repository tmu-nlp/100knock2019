'''
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
'''
import os
import pickle
from collections import Counter

os.makedirs('pickles', exist_ok=True)


def dump(file_name, data):
    with open(f"./pickles/{file_name}.pkl", 'wb') as f_out:
        pickle.dump(data, f_out)


in_file = "out82.txt"
out_file = "out83.txt"


with open(out_file, "w") as f_out:
    f = Counter(tuple(e.rstrip().split('\t')) for e in open(in_file))
    ft = Counter(e.rstrip().split('\t')[0] for e in open(in_file))
    fc = Counter(e.rstrip().split('\t')[1] for e in open(in_file))
    N = sum(1 for _ in open(in_file))

print(N)

dump('f', f)
dump('ft', ft)
dump('fc', fc)
dump('N', N)
