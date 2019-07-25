#85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．

import pickle
from collections import OrderedDict
from scipy import io
import numpy as np


fname_dict_index_t = 'dict_index_t'
fname_matrix_x_300 = 'matrix_x_300'

with open (fname_dict_index_t, "rb") as f:
    dict_index_t = pickle.load(f)

matrix_x_300 = io.loadmat(fname_matrix_x_300)["matrix_x_300"]
print(matrix_x_300[dict_index_t["United_States_of_America"]])
