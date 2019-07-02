import pickle
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

data_path = './chapter10/country_vec'
with open(data_path, 'rb') as f:
        country_index = pickle.load(f)
        vec = pickle.load(f)

tsne = TSNE().fit_transform(vec)
cls = KMeans(6).fit(vec)
plt.figure()
names = [f'${n}$' for name in country_index.values()]
for i, (label, n) in enumerate(zip(cls.labels_, names)):
        plt.scatter(tsne[i, 0], tsne[i, 1], marker=n)
plt.show()