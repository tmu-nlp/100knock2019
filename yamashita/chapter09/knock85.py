from sklearn.decomposition import TruncatedSVD
from sklearn.externals import joblib


def main():
    X = joblib.load('X_tc')

    pca = TruncatedSVD(n_components=300)
    X_pca = pca.fit_transform(X)

    print(f'shape : {X_pca.shape[0],X_pca.shape[1]}')
    joblib.dump(X_pca, 'X_PCA', compress=True)


if __name__ == '__main__':
    main()
