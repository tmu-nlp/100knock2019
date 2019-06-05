import pickle, json
import sys, pathlib
import numpy as np
from sklearn.cluster import KMeans

sys.path.append(str(pathlib.Path() / ".." / "chapter08"))

from knock72 import serialize, deserialize


def main():

    # 国名に関するベクトルの読み込み
    features = deserialize("country.matrix")
    t_index = deserialize("country.index")

    # k=5 でクラスタリング
    kmeans_model = KMeans(n_clusters=5).fit(features)
    labels = kmeans_model.labels_
    t_keys = t_index.keys()

    for label, t in zip(labels, t_keys):
        print(f"{t.ljust(12)} : {label}")


if __name__ == "__main__":
    main()
