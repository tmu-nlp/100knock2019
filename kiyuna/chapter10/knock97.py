'''
97. k-meansクラスタリング
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．
'''
from sklearn.cluster import KMeans
from knock96 import extract_vecs_of_countries

if __name__ == '__main__':
    X, labels = extract_vecs_of_countries()
    kmeans = KMeans(n_clusters=5).fit(X)
    y = kmeans.labels_

    for name, res in zip(labels, y):
        print(f"{name:<28}{res}")


'''
* KMeans
- https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
'''
