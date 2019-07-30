"""
96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．さらに，クラスタリング結果をデンドログラムとして可視化せよ．
"""

import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

f_in_dict = "dict_countries"
f_in_matrix = "matrix_counties"

with open(f_in_dict, "rb") as f:
    dict_index_t = pickle.load(f)

matrix_x_300 = io.loadmat(f_in_matrix)['matrix_x_300']

ward = ward(matrix_x_300)
print(ward)

dendrogram(ward, labels= list(dict_index_t.keys()), leaf_font_size=8 )
plt.show()