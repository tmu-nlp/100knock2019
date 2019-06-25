'''
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

- f(t,c): 単語tと文脈語cの共起回数
- f(t,*): 単語tの出現回数
- f(*,c): 文脈語cの出現回数
- N: 単語と文脈語のペアの総出現回数
'''
import os
import pickle
from collections import Counter

os.makedirs('pickles', exist_ok=True)


def dump(file_name, data):
    with open(f"./pickles/{file_name}.pkl", 'wb') as f_out:
        pickle.dump(data, f_out)


f_in_name = "out82.txt"
f_out_name = "out83.txt"

with open(f_out_name, 'w') as f_out:
    f = Counter(tuple(e.rstrip().split('\t')) for e in open(f_in_name))
    ft = Counter(e.rstrip().split('\t')[0] for e in open(f_in_name))
    fc = Counter(e.rstrip().split('\t')[1] for e in open(f_in_name))
    N = sum(1 for _ in open(f_in_name))

print(N)    # => 68075494, (expected: 11878244 * 3 * 2 = 71269464)

dump('f', f)
dump('ft', ft)
dump('fc', fc)
dump('N', N)
