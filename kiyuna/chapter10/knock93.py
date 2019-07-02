'''
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
'''
import sys
import pickle
import scipy.io as sio
from sklearn.metrics.pairwise import cosine_similarity as cos_sim


def message(text="", CR=False):
    text = "\r" + text if CR else text + "\n"
    sys.stderr.write("\33[92m" + text + "\33[0m")


def load(file_name):
    with open(f"../chapter09/pickles/{file_name}.pkl", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


in_path = 'out91.txt'
out_path = 'out93.txt'

ft = load('ft')
t2i = {token: i for i, token in enumerate(ft)}
vec = sio.loadmat('../chapter09/pickles/X_300.mat')['X_300']
cnt = [0, 0]

with open(out_path, 'w') as f_out:
    for line in open(in_path):
        a, b, x, y = line.split()   # a - b = x - y <=> y = b - a + x
        try:
            tgt = [vec[t2i[b]] - vec[t2i[a]] + vec[t2i[x]]]
            ranking = [(cos_sim([vec[t2i[key]]], tgt)[0][0], key)
                       for key in ft]
            cs, word = max(ranking)
        except Exception as e:
            word = '***'
            cs = -1
        cnt[y == word] += 1
        print(f'{a} {b} {x} {y} {word} {cs:f}', file=f_out)

message(f'ok = {cnt[True]}, ng = {cnt[False]}')     # => ok = ???, ng = ???


'''
# TODO: 実行時間
'''
