"""
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．
"""
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
from sklearn.cluster import KMeans

f_in_dict = "dict_countries"
f_in_matrix = "matrix_counties"

with open(f_in_dict, "rb") as f:
    dict_index_t = pickle.load(f)

matrix_x_300 = io.loadmat(f_in_matrix)['matrix_x_300']

predi = KMeans(n_clusters=5).fit_predict(matrix_x_300)

ans = zip(dict_index_t.keys(), predi)

for country, category in sorted(ans, key=lambda x: x[1]):
    print("{}\t {}" .format(category, country))
