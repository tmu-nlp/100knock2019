# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

from knock72 import serialize, deserialize
from sklearn.linear_model import LogisticRegression


def train() -> None:
    # 素性とラベルを読み込む
    features = deserialize("features")
    labels = deserialize("labels")

    # ロジスティック回帰モデル重みを学習させる (fit)
    model = LogisticRegression().fit(features, labels)
    serialize("model", model)


if __name__ == "__main__":
    train()
