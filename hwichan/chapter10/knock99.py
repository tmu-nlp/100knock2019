from scipy import io
import pickle
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


def main():
    with open('./pickles/country_dict', 'rb') as f:
        country_dict = pickle.load(f)

    country_matrix = io.loadmat('country_matrix')['country_matrix']

    # 次元の圧縮
    t_sne = TSNE(perplexity=30, learning_rate=500).fit_transform(country_matrix)

    # クラスタリング
    predicts = KMeans(n_clusters=5).fit_predict(country_matrix)

    fig, ax = plt.subplots()

    cmap = plt.get_cmap('Set1')
    for index, label in enumerate(country_dict.keys()):

        # cmpap(0.0~1.0)でカラーマップ内の色を取ってこれる
        cval = cmap(predicts[index] / 4)

        # scatter -> x軸とy軸を渡すことにより散布図を作成
        # t_sne[index, 0]で１列目 ,t_sne[index, 1]で２列目
        ax.scatter(t_sne[index, 0], t_sne[index, 1], marker='*', color=cval)

        # ラベルの指定
        ax.annotate(label, xy=(t_sne[index, 0], t_sne[index, 1]), color=cval)

    plt.show()


if __name__ == '__main__':
    main()


