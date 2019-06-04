# 76. ラベル付け
# 学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．

from knock72 import deserialize


def main() -> None:
    # モデル, 素性, 正解ラベルの読み込み
    model = deserialize("model")
    features = deserialize("features")
    labels = deserialize("labels")

    # 予測されたラベルと予測確率を取得
    preds = model.predict(features)
    probs = model.predict_proba(features)

    # 正解ラベル  予測ラベル  予測確率 を出力
    for ans, label, prob in zip(labels, preds, probs):
        print(f"{ans}\t{label}\t{max(prob):.6f}")


if __name__ == "__main__":
    main()

"""
実行結果

1	1	0.719703
-1	-1	0.839298
1	-1	0.548466
1	1	0.891464
-1	-1	0.691664
1	1	0.716255
1	1	0.754425
1	1	0.516552
1	1	0.566119
-1	-1	0.559691
1	1	0.589093
1	1	0.704603
-1	-1	0.621937
-1	-1	0.645569
-1	-1	0.553841
1	1	0.558314
1	1	0.931680
...
"""
