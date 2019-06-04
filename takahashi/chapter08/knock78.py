# 78. 5分割交差検定
# 76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
# すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．
# そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．

from sklearn.model_selection import cross_validate
from statistics import mean
from knock72 import deserialize


def main() -> None:
    model = deserialize("model")
    features = deserialize("features")
    labels = deserialize("labels")

    # 正解率，適合率，再現率，F1スコア
    eval_index = ["accuracy", "precision", "recall", "f1"]
    # 5 分割交差検定を行い、各指標の算術平均を取る
    scores = cross_validate(model, features, labels, cv=5, scoring=eval_index)
    scores = {k: mean(v) for k, v in scores.items()}

    print(f"正解率 : {scores['test_accuracy']}")
    print(f"適合率 : {scores['test_precision']}")
    print(f"再現率 : {scores['test_recall']}")
    print(f"F1     : {scores['test_f1']}")


if __name__ == "__main__":
    main()

"""
実行結果

正解率 : 0.760924705166596
適合率 : 0.7633215960891792
再現率 : 0.756516578719244
F1     : 0.759815592838911
"""
