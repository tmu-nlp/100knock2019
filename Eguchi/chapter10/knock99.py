#96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

f_in_dict = "dict_countries"
f_in_matrix = "matrix_counties"

with open(f_in_dict, "rb") as f:
    dict_index_t = pickle.load(f)

matrix_x_300 = io.loadmat(f_in_matrix)['matrix_x_300']
predi = KMeans(n_clusters=5).fit_predict(matrix_x_300)

t = TSNE(perplexity=30, learning_rate=500).fit_transform(matrix_x_300)
print(t)


fig,ax = plt.subplots()
cmap = plt.get_cmap("Set1")

for index, label in enumerate(dict_index_t.keys()):
    cval = cmap(predi[index] / 4)
    ax.scatter(t[index, 0], t[index, 1], marker=".", color= cval)
    ax.annotate(label, xy=(t[index,0], t[index, 1]), color=cval)
plt.show()