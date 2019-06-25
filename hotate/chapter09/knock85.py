from sklearn.decomposition import TruncatedSVD
from sklearn.externals import joblib


def main():
    ppmi = joblib.load('ppmi_mat.pkl')
    pca = TruncatedSVD(n_components=300)
    trans = pca.fit_transform(ppmi)
    print(pca.explained_variance_ratio_)
    joblib.dump(trans, 'pca.pkl')


if __name__ == '__main__':
    main()
