import joblib
import numpy as np


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def main():
    X_pca = joblib.load("X_PCA")
    t_index = joblib.load("t_index")
    united_states = X_pca[t_index["United_States"]]
    us = X_pca[t_index["U.S"]]
    print(cos_sim(united_states, us))


if __name__ == "__main__":
    main()
