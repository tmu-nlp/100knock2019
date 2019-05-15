from nltk.corpus import stopwords
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.utils import shuffle


class Feature:
    def __init__(self, corpus_filename: str = 'sentiment.txt') -> None:
        self.vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
        self.corpus_filename = corpus_filename
        self.label_list = list()
        self.sentence_list = list()

    def load_corpus(self):
        for line in open(self.corpus_filename, 'r'):
            label = line[:2]
            sentence = line[3:]
            self.label_list.append(label)
            self.sentence_list.append(sentence)
        self.label_list, self.sentence_list = shuffle(self.label_list, self.sentence_list)

    def make_vector(self):
        self.load_corpus()
        self.vectorizer.fit(self.sentence_list)
        joblib.dump(self.vectorizer, 'vectorizer.pkl')

    def save_data(self):
        joblib.dump(self.label_list, 'label.pkl')
        joblib.dump(self.sentence_list, 'sentences.pkl')


def main():
    feature = Feature()
    feature.make_vector()
    feature.save_data()


if __name__ == '__main__':
    main()
