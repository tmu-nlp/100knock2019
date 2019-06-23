'''
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．
そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．

memo: StratifiedKFold
'''
from sklearn.model_selection import cross_validate
from knock72 import load

model = load("model")
labels = load("labels")
features = load("features")

# 評価する指標: 正解率，適合率，再現率，F1スコア
score_funcs = ["accuracy", "precision", "recall", "f1"]
# Cross Validation で検証する
scores = cross_validate(model, features, labels, cv=5, scoring=score_funcs)

for key in score_funcs:
    print(f"{key:<10}: {scores['test_' + key].mean()}")


'''
* Cross Validation（交差検証）
https://blog.amedama.jp/entry/sklearn-cv-custom-metric
'''
