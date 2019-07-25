#"85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．"

import pickle
from collections import OrderedDict
from scipy import io
import numpy as np


fname_dict_index_t = 'dict_index_t'
fname_matrix_x_300 = 'matrix_x_300'

with open (fname_dict_index_t, "rb") as f:
    dict_index_t = pickle.load(f)

matrix_x_300 = io.loadmat(fname_matrix_x_300)["matrix_x_300"]
matrix_england = matrix_x_300[dict_index_t["Spain"]] - matrix_x_300[dict_index_t["Madrid"]] + matrix_x_300[dict_index_t["Athens"]] 

rank = list()
for i in range(0, len(dict_index_t)) :
    matrix_ranking = matrix_x_300[i]
    norm = np.linalg.norm(matrix_england) * np.linalg.norm(matrix_ranking)
    if norm != 0:
        value = np.dot(matrix_england, matrix_ranking) / norm
    else:
        value = -1
    rank.append(value)

index_sorted = np.argsort( rank)
keys = list(dict_index_t.keys())
for index in index_sorted[-2:-12:-1]:      
    print('{}\t{}'.format(keys[index], rank[index]))

