from sklearn.externals import joblib


def main():
    pca = joblib.load('pca.pkl')
    vocab = joblib.load('vocab.pkl')
    united = pca[vocab['United_States'.lower()]]
    print(united)


if __name__ == '__main__':
    main()
