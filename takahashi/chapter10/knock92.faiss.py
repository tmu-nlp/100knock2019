"""
92. アナロジーデータへの適用

91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
求めた単語と類似度は，各事例の末尾に追記せよ．

このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
"""

import numpy as np
import sys, pathlib
from knock90 import multi_vec
from scipy.io import loadmat
from tqdm import tqdm
import faiss

chap08 = pathlib.Path().parent / ".." / "chapter08"
chap09 = pathlib.Path().parent / ".." / "chapter09"
sys.path.extend([str(chap08), str(chap09)])

from knock72 import serialize, deserialize
from knock87 import cosine_similarity
from knock80 import file_reader


ppmi, p_index = loadmat("knock85.matrix")["knock85.matrix"], deserialize("p_index")
p_keys = list(p_index.keys())

w2v, t_index = np.array(deserialize("matrix")), deserialize("t_index")
t_keys = list(t_index.keys())

faiss_ppmi = faiss.IndexFlatIP(300)
faiss_ppmi.add(np.ascontiguousarray(ppmi.astype("float32")))

faiss_w2v = faiss.IndexFlatIP(300)
faiss_w2v.add(np.ascontiguousarray(w2v.astype("float32")))

with open("./results/faiss.ppmi.out.txt", "w") as ppmi_out, open(
    "./results/faiss.w2v.out.txt", "w"
) as w2v_out:
    for line in open("./results/knock91.output.txt", "r", encoding="utf-8"):
        ws = line.rstrip().split()
        try:
            v1 = ppmi[p_index[ws[1]]] - ppmi[p_index[ws[0]]] + ppmi[p_index[ws[2]]]
            sim_index = faiss_ppmi.search(np.array([v1]).astype("float32"), 1)[1][0][0]
            print(line.rstrip(), p_keys[sim_index], file=ppmi_out)
        except KeyError:
            print(line.rstrip(), "-", file=ppmi_out)

        try:
            v2 = w2v[t_index[ws[1]]] - w2v[t_index[ws[0]]] + w2v[t_index[ws[2]]]
            sim_index = faiss_w2v.search(np.array([v2]).astype("float32"), 1)[1][0][0]
            print(line.rstrip(), t_keys[sim_index], file=w2v_out)
        except KeyError:
            print(line.rstrip(), "-", file=w2v_out)
