'''
99. t-SNEによる可視化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
'''
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from knock96 import extract_vecs_of_countries


if __name__ == '__main__':
    np.random.seed(42)
    X, labels = extract_vecs_of_countries()

    t_sne = TSNE(learning_rate=500).fit_transform(X)
    predicts = KMeans(n_clusters=5).fit_predict(X)      # 色分け用

    fig, ax = plt.subplots()
    cmap = plt.get_cmap('Set1')
    for i, label in enumerate(labels):
        cval = cmap(predicts[i])
        ax.scatter(t_sne[i, 0], t_sne[i, 1], marker='.', color=cval)
        ax.annotate(label, xy=t_sne[i, :], color=cval)
    plt.savefig("out99.png")


'''
* TSNE
- https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html

* KMeans
- https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
'''
