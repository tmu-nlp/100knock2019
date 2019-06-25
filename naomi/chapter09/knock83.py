# 82の出力を利用し，以下の出現分布，および定数を求めよ．

# f(t,c): 単語tと文脈語cの共起回数
# f(t,∗): 単語tの出現回数
# f(∗,c): 文脈語cの出現回数
# N: 単語と文脈語のペアの総出現回数

from tqdm import tqdm
from collections import defaultdict
import pickle


def save(file_name, data):
    with open(f"./pickles/{file_name}", 'wb') as f_out:
        pickle.dump(data, f_out)


def load(file_name):
    with open(f"./pickles/{file_name}", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


if __name__ == "__main__":
    # Initialize dictionaries
    t_count = defaultdict(lambda: 0)
    c_count = defaultdict(lambda: 0)
    tc_count = defaultdict(lambda: 0)
    N = 0

    with open('./knock82.txt', 'r') as fin:

        # Add to dictionaries
        for line in tqdm(fin):
            t, c = line.rstrip().split('\t')
            N += 1
            t_count[t] += 1
            c_count[c] += 1
            tc_count[t+' '+c] += 1
        
        # Save as pickles
        save('t', t_count)
        save('c', c_count)
        save('tc', tc_count)
        save('N', N)
        print(N)
