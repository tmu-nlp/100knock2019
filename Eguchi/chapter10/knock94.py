"""
The WordSimilarity-353 Test Collectionの評価データを入力とし，1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ
"""
from gensim.models import word2vec
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np


fname_dict_index_t = r'C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter09\dict_index_t'
fname_matrix_x_300 = r'C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter09\matrix_x_300'
in_fn = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter10\combined.tab"
f_word2vec_out = r'C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter10\vectors.txt'
out_fn1 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter10\combined_out_85.tab"
out_fn2 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter10\combined_out_90.tab"

with open (fname_dict_index_t, "rb") as f:
    dict_index_t = pickle.load(f)

keys = list(dict_index_t.keys())

matrix_x_300 = io.loadmat(fname_matrix_x_300)["matrix_x_300"]



with open(in_fn, 'rt') as in_f, open(out_fn1, 'wt') as out_f:
    
    flag = True
    for line in in_f:
        
        if flag == True:
            flag = False
            
            continue
        
        words = line.split("\t")
        try:
            norm = np.linalg.norm(matrix_x_300[dict_index_t[words[0]]]) * np.linalg.norm(matrix_x_300[dict_index_t[words[1]]])

            if norm != 0:
                value = np.dot(matrix_x_300[dict_index_t[words[0]]], matrix_x_300[dict_index_t[words[1]]]) / norm
            else:
                value = -1
        except KeyError:
            
            value = -1
        
        print("{}\t{}" .format(line.strip(), value), file=out_f)
        print("{}\t{}" .format(line.strip(), value))


with open(in_fn, 'rt') as in_f, open(out_fn2, 'wt') as out_f:
    model = word2vec.Word2Vec.load(f_word2vec_out)
    flag = True
    for line in in_f:
        
        if flag == True:
            flag = False
            
            continue
        
        words = line.split("\t")
        try:
            value = model.similarity(words[0], words[1])
        except KeyError:
            value = -1
        
        print("{}\t{}" .format(line.strip(), value), file=out_f)
        print("{}\t{}" .format(line.strip(), value))
