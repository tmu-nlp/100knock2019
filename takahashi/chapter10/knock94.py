"""
94. WordSimilarity-353での類似度計算

The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．

"""

import numpy as np
import sys, pathlib
from scipy.io import loadmat

chap08 = pathlib.Path().parent / ".." / "chapter08"
chap09 = pathlib.Path().parent / ".." / "chapter09"
sys.path.extend([str(chap08), str(chap09)])

from knock72 import serialize, deserialize
from knock87 import cosine_similarity
from knock80 import file_reader

w2v, w2v_index = deserialize("matrix"), deserialize("t_index")
ppmi, ppmi_index = loadmat("knock85.matrix")["knock85.matrix"], deserialize("p_index")


def print_w2v(line: str, t1: str, t2: str, f):
    """ t1, t2 の各単語ベクトルのコサイン類似度を求める (word2vec) """
    try:
        res = cosine_similarity(w2v[w2v_index[t1]], w2v[w2v_index[t2]])
        print(f"{line.rstrip()}\t{res}", file=f)
    except KeyError:
        print(f"{line.rstrip()}\t-", file=f)


def print_ppmi(line: str, t1: str, t2: str, f):
    """ t1, t2 の各単語ベクトルのコサイン類似度を求める (ppmi) """
    try:
        res = cosine_similarity(ppmi[ppmi_index[t1]], ppmi[ppmi_index[t2]])
        print(f"{line.rstrip()}\t{res}", file=f)
    except KeyError:
        print(f"{line.rstrip()}\t-", file=f)


def main():
    input_file = "../data/combined.tab"
    ppmi_file = "./results/knock94.ppmi.txt"
    w2v_file = "./results/knock94.w2v.txt"
    with open(input_file, "r") as in_file, \
        open(ppmi_file, "w") as out_ppmi, \
        open(w2v, "w") as out_w2v:
        
        in_file.readline()
        for line in in_file:
            token1, token2, *_ = line.rstrip().split("\t")

            print_ppmi(line, token1, token2, out_ppmi)
            print_w2v(line, token1, token2, out_w2v)


if __name__ == "__main__":
    main()
