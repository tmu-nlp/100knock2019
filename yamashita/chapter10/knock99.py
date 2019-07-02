from sklearn.externals import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans


def main():
    country_vecs = joblib.load('country_vecs')
    t_sne = TSNE(perplexity=30, learning_rate=500).fit_transform(
        list(country_vecs.values()))
    kmeans = KMeans(n_clusters=5).fit_predict(list(country_vecs.values()))
    cmap = plt.get_cmap('Set1')

    fig, ax = plt.subplots()
    for index, label in enumerate(country_vecs.keys()):
        color = cmap(kmeans[index] / 4)
        ax.scatter(t_sne[index, 0], t_sne[index, 1], marker='.', color=color)
        ax.annotate(label, xy=(t_sne[index, 0], t_sne[index, 1]), color=color)
    plt.show()


if __name__ == '__main__':
    main()
