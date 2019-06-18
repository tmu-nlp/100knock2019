import numpy as np
from knock71 import is_stopword
from stemming.porter2 import stem
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib


def clean_sentence(line: str) -> str:
    sentence = []

    for word in line.split():
        word = word.rstrip('\n,.;:?!')
        word = stem(word)

        if is_stopword(word) or word == '':
            continue
        sentence.append(word)

    return ' '.join(sentence)


def abstract_features(inpath: str):
    with open(inpath, 'r', encoding='utf-8', errors='ignore') as fin:

        labels = []
        sentences = []
        for line in fin:

            label = [line[:2]]
            words = line[3:]

            sentence = clean_sentence(words)

            labels.append(label)
            sentences.append(sentence)
        

        vectorizer = TfidfVectorizer()
        feature = vectorizer.fit_transform(sentences).toarray()
        sentiment = np.array(labels)

        joblib.dump(feature, 'feature')
        joblib.dump(sentiment, 'sentiment')
        joblib.dump(vectorizer.vocabulary_,'vocab')
        joblib.dump(vectorizer.get_feature_names(),'name')


def main():
    inputfile = 'sentiment.txt'
    abstract_features(inputfile)


if __name__ == '__main__':
    main()
