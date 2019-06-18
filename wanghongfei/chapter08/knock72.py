from knock71 import stop_word
from nltk.stem import PorterStemmer
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def get_feature(sentence):
    ps = PorterStemmer()
    word_list = []
    for word in sentence.strip("\n").split(" "):
        if stop_word(word) == True:
            continue
        else:
            word_list.append(ps.stem(word))
    return " ".join(word_list)

if __name__ == "__main__":
    sentences = []
    labels = []
    sentiment_file = open("./chapter08/sentiment.txt", "r").readlines()
    # 文とラベルをリストで保存
    for line in sentiment_file:
        sentence = line[3:]
        label = line[:2]
        labels.append(label)
        sentences.append(get_feature(sentence))
    # 文をベクトルに変換
    vectorizer = CountVectorizer()
    feature = vectorizer.fit_transform(sentences).toarray()
    sentiment = np.array(labels)
    # save feature, sentiment, vocab and vocab_size
    with open("./chapter08/feature", "wb") as f1, open("./chapter08/sentiment", "wb") as f2:
        pickle.dump(feature, f1)
        pickle.dump(sentiment, f2)
    with open("./chapter08/vocab_size", "wb") as f1, open("./chapter08/vocab", "wb") as f2:
        pickle.dump(vectorizer.vocabulary_, f1)
        pickle.dump(vectorizer.get_feature_names(), f2)