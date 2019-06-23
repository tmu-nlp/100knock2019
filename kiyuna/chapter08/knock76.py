'''
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
'''
from knock72 import load

model = load("model")
labels = load("labels")
features = load("features")

preds = model.predict(features)         # 予測されたラベル
probs = model.predict_proba(features)   # 予測確率

for ans, predict, proba in zip(labels, preds, probs):
    print(f"{ans:+d}\t{predict:+d}\t{max(proba):f}")
