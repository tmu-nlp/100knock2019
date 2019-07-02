import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import dill
from scipy.cluster.hierarchy import ward, dendrogram


def load(file_name):
    with open(f"./dills/{file_name}", 'rb') as f_in:
        data = dill.load(f_in)
    return data


countries = load('countries')
X = load('X')

# Ward法でクラスタリング
ward = ward(X)
print(ward)

# デンドログラム表示
dendrogram(ward, labels=countries, leaf_font_size=8)
plt.show()