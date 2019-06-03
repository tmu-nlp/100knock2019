from sklearn.linear_model import LogisticRegression
import joblib
          
# データの読み込み
feature = joblib.load('tfidf_feature')
sentiment = joblib.load('tfidf_sentiment')
# 学習
model = LogisticRegression(random_state=16).fit(feature, sentiment)
# モデルの保存
joblib.dump(model, 'logr_model')