'''
98. Ward法によるクラスタリング
96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．さらに，クラスタリング結果をデンドログラムとして可視化せよ．
'''

from knock96 import extract_vecs_of_countries
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt


if __name__ == '__main__':
    X, labels = extract_vecs_of_countries()
    Z = linkage(X, method="ward", metric="euclidean")
    plt.figure(figsize=(40, 25))
    dendrogram(Z, labels=labels,
               leaf_font_size=10.5,
               color_threshold=2.,
               )
    plt.savefig("out98.png")
