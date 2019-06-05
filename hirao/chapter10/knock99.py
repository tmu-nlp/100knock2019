import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import joblib

def main():
    # 色系統決め
    cmap = plt.get_cmap('Set1')
    country_vec = joblib.load("country_vec")
    matrix = list(country_vec.values())
    t_sne = TSNE(perplexity=30, learning_rate=1).fit_transform(matrix)
    predicts = KMeans(n_clusters=5).fit_predict(matrix)

    for index, label in enumerate(country_vec.keys()):
        cval = cmap(predicts[index] / 4)
        plt.scatter(t_sne[index, 0], t_sne[index, 1], marker='.', color=cval)
        plt.annotate(label, xy=(t_sne[index, 0], t_sne[index, 1]), color=cval)
    plt.show()


if __name__ == "__main__":
    main()
