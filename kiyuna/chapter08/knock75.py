'''
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，
重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
'''
import sys
from knock72 import load


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


model = load("model")
names = load("names")
weights = model.coef_[0]
rank = sorted(zip(weights, names), reverse=True)

message("[+] best 10")
for weight, name in rank[:10]:
    print(f"{name:<15}{weight: f}")

message("[+] worst 10")
for weight, name in rank[-10:]:
    print(f"{name:<15}{weight: f}")


'''
* sklearn.linear_model.LogisticRegression
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

- coef_ : array, shape (1, n_features) or (n_classes, n_features)
    [Attributes] Coefficient of the features in the decision function.
'''
