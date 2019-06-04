# 79. 適合率-再現率グラフの描画
# ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．

from sklearn.metrics import precision_recall_curve
from knock72 import deserialize
import matplotlib.pyplot as plt


def main():
    model = deserialize("model")
    features = deserialize("features")
    labels = deserialize("labels")

    # +1 に分類される確率
    probs = model.predict_proba(features)[:, 1]
    # 正解ラベルと予測したラベルの確率を与える
    pre, rec, th = precision_recall_curve(labels, probs)

    plt.plot(rec, pre)
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.show()


if __name__ == "__main__":
    main()


# ref : https://blog.amedama.jp/entry/2017/12/18/005311
