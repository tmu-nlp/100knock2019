# 84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．

from sklearn.decomposition import PCA
import pickle


def save(file_name, data):
    with open(f"./pickles/{file_name}", 'wb') as f_out:
        pickle.dump(data, f_out)


def load(file_name):
    with open(f"./pickles/{file_name}", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


if __name__ == "__main__":
    # import X
    X = load('Xtc')

    # set PCA with num of principal components = 300
    pca = PCA(n_components=300)

    # execute PCA
    X300 = pca.fit_transform(X)

    save('X300', X300)

