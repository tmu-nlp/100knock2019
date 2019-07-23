#72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
from sklearn.linear_model import LogisticRegression
import joblib

feature = joblib.load('tfidf_feature')
sentiment = joblib.load('tfidf_sentiment')

model = LogisticRegression(random_state=16).fit(feature, sentiment)
joblib.dump(model, 'logr_model')
