"""
99. t-SNEによる可視化

96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
"""

import pickle
from scipy import io
import numpy as np

from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

import sys, pathlib

sys.path.append(str(pathlib.Path() / ".." / "chapter08"))

from knock72 import deserialize


def main():
    # ベクトルの読み込み
    t_index = deserialize("country.index")
    matrix = np.array(deserialize("country.matrix"))

    t_sne = TSNE(perplexity=30, learning_rate=500).fit_transform(matrix)
    predicts = KMeans(n_clusters=5).fit_predict(matrix)

    fig, ax = plt.subplots()
    cmap = plt.get_cmap("Set1")
    for index, label in enumerate(t_index.keys()):
        cval = cmap(predicts[index] / 4)
        ax.scatter(t_sne[index, 0], t_sne[index, 1], marker=".", color=cval)
        ax.annotate(label, xy=(t_sne[index, 0], t_sne[index, 1]), color=cval)
    plt.show()


if __name__ == "__main__":
    main()
