# faissを使いたかったけどバチクソに環境設定がだるかった
# https://qiita.com/wasnot/items/20c4f30a529ae3ed5f52
import joblib
import numpy as np
from tqdm import tqdm
from operator import matmul


def cos_sim(v1, v2):
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return matmul(v1, v2) / norm if norm else -1


def main():
    X_pca = joblib.load("X_PCA")
    t_index = joblib.load("t_index")

    print("start Calc")
    england = X_pca[t_index["England"]]

    l = []
    rows = X_pca.shape[0]
    for i, name in enumerate(tqdm(t_index.keys())):
        dis = cos_sim(england, X_pca[i])
        l.append([name, dis])

    for name, dis in sorted(l, key=lambda x: x[1], reverse=True)[:10]:
        print(f"{name}\t{dis}")


if __name__ == "__main__":
    main()
