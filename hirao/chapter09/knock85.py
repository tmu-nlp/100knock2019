from sklearn.decomposition import TruncatedSVD
import joblib


def main():
    X = joblib.load("X")

    pca = TruncatedSVD(n_components=300)
    pca.fit(X)
    X_pca = pca.transform(X)
    print(f"After PCA shape {X_pca.shape[0], X_pca.shape[1]}")
    joblib.dump(X_pca, "X_PCA", compress=3)


if __name__ == "__main__":
    main()
