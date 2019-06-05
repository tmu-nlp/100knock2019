import joblib


def main():
    X_pca = joblib.load("X_PCA")
    t_index = joblib.load("t_index")
    print(X_pca[t_index["United_States"]])


if __name__ == "__main__":
    main()
