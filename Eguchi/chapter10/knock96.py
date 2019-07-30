"""
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
"""
import pickle
import numpy as np
from collections import OrderedDict
from scipy import io

f_countries =fname = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter09\countries.txt"
fname_dict_index_t = r'C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter09\dict_index_t'
fname_matrix_x_300 = r'C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter09\matrix_x_300'
f_out_dict = "dict_countries"
f_out_matrix = "matrix_counties"


with open (fname_dict_index_t, "rb") as f:
    dict_index_t = pickle.load(f)

matrix_x_300 = io.loadmat(fname_matrix_x_300)["matrix_x_300"]

with open(f_countries, "rt") as f:
    dict_word = OrderedDict()
    matrix_add = np.empty([0,300], dtype=np.float64)
    counter = 0
    for line in f:
        try:
            country = line.strip().replace(" ", "_")
            index = dict_index_t[country]
            matrix_add = np.vstack([matrix_add, matrix_x_300[index]])
            dict_word[country] = counter 
            counter += 1
        except:
            pass
    
io.savemat(f_out_matrix, {"matrix_x_300":matrix_add})
with open(f_out_dict, "wb") as f:
    pickle.dump(dict_word, f)