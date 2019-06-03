from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import numpy as np
from knock72 import FeatureEnginnering

def predict():
    model = joblib.load('logr_model')
    vocab = joblib.load('tfidf_vocab')

    vectorizer = TfidfVectorizer(vocabulary=vocab)
    fe = FeatureEnginnering()
    data_size = sum(1 for l in open("sentiment.txt", encoding='utf8'))

    true_labels = np.zeros(data_size)
    pred_result = np.zeros(data_size)
    probability = np.zeros(data_size)
    i = 0
    f = open("sentiment.txt", encoding='utf8')
    for line in f:
        true_label = int(line[:2])
        true_labels[i] = true_label
        sentence = line[3:].strip()
        feature = fe.remove_stop_word(sentence)
        feature_vec = vectorizer.fit_transform([feature]).toarray()

        predict = model.predict(feature_vec)[0]
        pred_result[i] = int(predict)
        prob = model.predict_proba(feature_vec).flatten()
        probability[i] = prob[1]
        i += 1
    return true_labels, pred_result, probability

if __name__ == "__main__":
    true, pred, prob = predict()
    for t, pre, pro in zip(true, pred, prob):
        if pro < 0.5:
            pro = 1 - pro
        print(f"{t}\t{pre}\t{pro:.3}")