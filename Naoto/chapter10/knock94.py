'''
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
'''


import sys
import pickle
import scipy.io as sio
from sklearn.metrics.pairwise import cosine_similarity as cos_sim
import zipfile

import word2vec
import time


start = time.time()


def message(text="", CR=False):
    text = "\r" + text if CR else text + "\n"
    sys.stderr.write("\33[92m" + text + "\33[0m")


def load(file_name):
    with open(f"../chapter09/pickles/{file_name}.pkl", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


in_path = 'wordsim353.zip'
out_path_ch09 = 'out94_ch09.txt'
out_path_ch10 = 'out94_ch10.txt'

word2vec_model = word2vec.load('out90.bin')
ft = load('ft')
t2i = {token: i for i, token in enumerate(ft)}
X_300 = sio.loadmat('../chapter09/pickles/X_300.mat')['X_300']

with zipfile.PyZipFile(in_path, "r") as myzip, open(out_path_ch09, "w") as f_out_ch09, open(out_path_ch10, "w") as f_out_ch10:
    with myzip.open('combined.tab') as f_in:
        for line in map(lambda x: x.decode().rstrip(), f_in):
            words = line.split('\t')
            try:
                cs_09 = cos_sim([X_300[t2i[words[0]]]], [X_300[t2i[words[1]]]])[0][0]
            except Exception as e:
                cs_09 = -1
            try:
                cs_10 = cos_sim([word2vec_model[words[0]]], [word2vec_model[words[1]]])[0][0]
            except Exception as e:
                cs_10 = -1
            print(f"{line}\t{cs_09:f}", file=f_out_ch09)
            print(f"{line}\t{cs_10:f}", file=f_out_ch10)


end = time.time()
print(f"elapsed time = {end - start} s")
