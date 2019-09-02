'''
97. k-meansクラスタリング
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．
'''

from knock96 import extract_vecs_of_countries
from sklearn.cluster import KMeans


vecs, countries = extract_vecs_of_countries()
kmeans_model = KMeans(n_clusters=5, random_state=10).fit(vecs)
labels = kmeans_model.labels_
for country, label in zip(countries, labels):
    print(country, label)
