# 97. k-meansクラスタリング
# 96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．

import numpy as np
import dill
from sklearn.cluster import KMeans


def save(file_name, data):
    with open(f"./dills/{file_name}", 'wb') as f_out:
        dill.dump(data, f_out)


def load(file_name):
    with open(f"./dills/{file_name}", 'rb') as f_in:
        data = dill.load(f_in)
    return data


countries = load('countries')
X = load('X')

kmeans = KMeans(n_clusters=2, random_state=0).fit(np.array(X))
with open('out97.txt', 'w+', encoding='utf-8') as f:
    for country, cluster in zip(countries, kmeans.labels_):
        print(f'{country} {cluster}', file=f)
