import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.datasets import load_iris
import joblib

def main():
    country_vec = joblib.load("country_vec")

    df = pd.DataFrame(country_vec.values(), index=country_vec.keys())

    # 階層型クラスタリングの実施
    # ウォード法 x ユークリッド距離
    linkage_result = linkage(df, method='ward', metric='euclidean')

    # クラスタ分けするしきい値を決める
    threshold = 0.7 * np.max(linkage_result[:, 2])

    # 階層型クラスタリングの可視化
    plt.figure(num=None, figsize=(16, 9), dpi=200, facecolor='w', edgecolor='k')
    dendrogram(linkage_result, labels=list(country_vec.keys()), color_threshold=threshold)
    plt.show()

if __name__ == "__main__":
    main()