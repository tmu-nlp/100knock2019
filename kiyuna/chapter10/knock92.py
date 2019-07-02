'''
92. アナロジーデータへの適用
91で作成した評価データの各事例に対して，
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
'''
import sys
import word2vec
from sklearn.metrics.pairwise import cosine_similarity


def message(text="", CR=False):
    text = "\r" + text if CR else text + "\n"
    sys.stderr.write("\33[92m" + text + "\33[0m")


model_path = 'out90.bin'
in_path = 'out91.txt'
out_path = 'out92.txt'

model = word2vec.load(model_path)
cnt = [0, 0]

with open(out_path, 'w') as f_out:
    for line in open(in_path):
        a, b, x, y = line.split()   # a - b = x - y <=> y = b - a + x
        try:
            tgt = [model[b] - model[a] + model[x]]
            indexes, _ = model.analogy(pos=[b, x], neg=[a])
            word = model.vocab[indexes[0]]
            cs = cosine_similarity([model[word]], tgt)[0][0]
        except Exception as e:
            word = '***'
            cs = -1
        cnt[y == word] += 1
        print(f'{a} {b} {x} {y} {word} {cs:f}', file=f_out)

message(f'ok = {cnt[True]}, ng = {cnt[False]}')     # => ok = 217, ng = 289
