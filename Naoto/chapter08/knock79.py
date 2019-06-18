'''
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．
'''

from sklearn.metrics import precision_recall_curve
from sklearn.feature_extraction.text import TfidfVectorizer
from knock73 import deserialize
import matplotlib.pyplot as plt
import numpy as np


def precision_recall():
    model = deserialize("model")
    features = deserialize("features")
    labels = deserialize("labels")
    precision, recall, threshold = precision_recall_curve(labels, model.predict_proba(features)[:, 1])
    for i in range(21):
        close_point = np.argmin(np.abs(threshold - (i * 0.05)))
        plt.plot(precision[close_point], recall[close_point], 'o')

    # 適合率-再現率曲線
    plt.plot(precision, recall)
    plt.xlabel('Precision')
    plt.ylabel('Recall')

    plt.show()


if __name__ == "__main__":
    precision_recall()
