'''
74. 予測
73で学習したロジスティック回帰モデルを用い，
与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from knock72 import load, extract_features


model = load("model")
vocab = load("vocabs")

_, docs = extract_features("./test.txt")
vectorizer = TfidfVectorizer(vocabulary=vocab)
features = vectorizer.fit_transform(docs).toarray()

pp = zip(model.predict(features), model.predict_proba(features))
for predict, proba in pp:
    print(f"{predict:+d} : {max(proba):f}")


'''
* sklearn.linear_model.LogisticRegression
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

- predict(self, X)
    [Methods] Predict class labels for samples in X.

- predict_proba(self, X)
    [Methods] Probability estimates.
'''
