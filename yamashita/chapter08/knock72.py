import numpy as np
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from knock71 import is_stopword
import snowballstemmer
from tqdm import tqdm


def get_feature_base(sentence):
    stemmer = snowballstemmer.stemmer('english')
    words = sentence.split()
    result = []
    for word in words:
        if is_stopword(word):
            continue
        result.append(stemmer.stemWord(word))
    return ' '.join(result)


def create_feature():
    labels = []
    corpus = []
    with open('sentiment.txt', 'r', encoding='utf-8') as senti_file:
        for line in tqdm(senti_file):
            label = line[:2]
            sentence = line.rstrip()[3:]
            labels.append(int(label))
            sentence_ = get_feature_base(sentence)
            corpus.append(sentence_)

        vectorizer = TfidfVectorizer()
        feature = vectorizer.fit_transform(corpus).toarray()
        sentiment = np.array(labels)

        joblib.dump(feature, 'feature')
        joblib.dump(sentiment, 'sentiment')
        joblib.dump(vectorizer.vocabulary_, 'vocabulary')
        joblib.dump(vectorizer.get_feature_names(), 'name')


if __name__ == '__main__':
    create_feature()
