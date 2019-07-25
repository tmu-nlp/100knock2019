#85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．

import pickle
from collections import OrderedDict
from scipy import io
import numpy as np



fname_dict_index_t = 'dict_index_t'
fname_matrix_x_300 = 'matrix_x_300'

with open (fname_dict_index_t, "rb") as f:
    dict_index_t = pickle.load(f)

matrix_x_300 = io.loadmat(fname_matrix_x_300)["matrix_x_300"]

matrix_USA = matrix_x_300[dict_index_t["United_States_of_America"]]
matrix_U_S = matrix_x_300[dict_index_t["U.S"]]
print(matrix_U_S)
norm = np.linalg.norm(matrix_USA) * np.linalg.norm(matrix_U_S)
print(norm)
print(np.dot(matrix_USA, matrix_U_S) / norm)
