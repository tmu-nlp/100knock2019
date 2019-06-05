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

chap08 = pathlib.Path().parent / ".." / "chapter08"
chap09 = pathlib.Path().parent / ".." / "chapter09"
sys.path.extend([str(chap08), str(chap09)])

from knock72 import serialize, deserialize
from knock87 import cosine_similarity
from knock80 import file_reader


w2v, w2v_index = deserialize("matrix"), deserialize("t_index")
ppmi, ppmi_index = loadmat("knock85.matrix")["knock85.matrix"], deserialize("p_index")


def apply_w2v(line: str, f) -> None:
    t1, t2, t3, *_ = line.rstrip().split()
    res = multi_vec(w2v, w2v_index, t1, t2, t3)
    if not res:
        print(line.rstrip(), "-", "-", file=f)
    else:
        word, sim = res[0]
        print(line.rstrip(), word, sim, file=f)


def apply_ppmi(line: str, f) -> None:
    t1, t2, t3, *_ = line.rstrip().split()
    res = multi_vec(ppmi, ppmi_index, t1, t2, t3)
    if not res:
        print(line.rstrip(), "-", "-", file=f)
    else:
        word, sim = res[0]
        print(line.rstrip(), word, sim, file=f)


def main(line_num: int):
    in_file = "./results/knock91.output.txt"
    out_w2v = "./results/knock92.w2v.output.txt"
    out_ppmi = "./results/knock92.ppmi.output.txt"

    line = file_reader(in_file)

    with open(out_w2v, "w", encoding="utf-8") as file_w2v, \
    open(out_ppmi, "w", encoding="utf-8") as file_ppmi:
        for _ in tqdm(range(line_num)):
            current = line.__next__()
            apply_w2v(current, file_w2v)
            apply_ppmi(current, file_ppmi)


if __name__ == "__main__":
    line_num = 506
    main(line_num)