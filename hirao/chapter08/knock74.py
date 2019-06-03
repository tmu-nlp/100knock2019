from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from knock72 import FeatureEnginnering

model = joblib.load('logr_model')
vocab = joblib.load('tfidf_vocab')

f = open("sentiment.txt", encoding='utf8')
for _ in range(1):
    next(f)
sentence = f.readline()
print("Input sentence\n", sentence)
sentence = sentence.strip()[3:]
fe = FeatureEnginnering()
feature = fe.remove_stop_word(sentence)

vectorizer = TfidfVectorizer(vocabulary=vocab)
feature_vec = vectorizer.fit_transform([feature]).toarray()

predict = model.predict(feature_vec)[0]
probability = model.predict_proba(feature_vec).flatten()

print(f"Predict result: {predict}")
print(f"Probability of result\n-1: {probability[0]:.2}%\n+1: {probability[1]:.2}%")