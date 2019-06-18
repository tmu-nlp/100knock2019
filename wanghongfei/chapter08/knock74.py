from knock72 import get_feature
from sklearn.feature_extraction.text import CountVectorizer
import pickle

with open("./chapter08/model", "rb") as f:
    model = pickle.load(f)
with open("./chapter08/vocab_size", "rb") as f:
    vocab_size = pickle.load(f)
sentence = "This is a very good wonderful fantastic movie."
sentence_feature = get_feature(sentence)
vectorizer = CountVectorizer(vocabulary = vocab_size)
feature_vec = vectorizer.fit_transform([sentence_feature]).toarray()
label_predict = model.predict(feature_vec)
prob = model.predict_proba(feature_vec)
print(label_predict, prob)
