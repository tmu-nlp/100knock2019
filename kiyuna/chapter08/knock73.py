'''
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
'''
from sklearn.linear_model import LogisticRegression
from knock72 import load, save

labels = load("labels")
features = load("features")

model = LogisticRegression().fit(features, labels)
save("model", model)
