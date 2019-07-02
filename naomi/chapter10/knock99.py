import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import dill
from sklearn.cluster import KMeans


def load(file_name):
    with open(f"./dills/{file_name}", 'rb') as f_in:
        data = dill.load(f_in)
    return data


countries = load('countries')
X = load('X')


# t-SNE
t_sne = TSNE(perplexity=30, learning_rate=500).fit_transform(X)
print(t_sne)

# KMeansクラスタリング
predicts = KMeans(n_clusters=5).fit_predict(X)

# 表示
fig, ax = plt.subplots()
cmap = plt.get_cmap('Set1')
for index, label in enumerate(countries):
    cval = cmap(predicts[index] / 4)
    ax.scatter(t_sne[index, 0], t_sne[index, 1], marker='.', color=cval)
    ax.annotate(label, xy=(t_sne[index, 0], t_sne[index, 1]), color=cval)
plt.show()
