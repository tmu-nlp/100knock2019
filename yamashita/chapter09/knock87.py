from sklearn.decomposition import TruncatedSVD
from sklearn.externals import joblib
import numpy as np


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def main():
    X_PCA = joblib.load('X_PCA')
    t_index = joblib.load('t_index')

    print(cos_sim(X_PCA[t_index['United_States']], X_PCA[t_index['U.S']]))


if __name__ == '__main__':
    main()


# 0.8107405163200374
