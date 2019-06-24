import random

from scipy.sparse import lil_matrix
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict


class Matrix:
    def __init__(self, filename='knock81.100.txt'):
        self.filename = filename
        self.sentences = list()
        self.vec = None
        self.vocab = None
        self.matrix = None

    def create_vocab(self):
        for line in open(self.filename):
            self.sentences.append(line.strip())
        self.vec = CountVectorizer(stop_words=[]).fit(self.sentences)
        self.vocab = self.vec.vocabulary_

    def create_matrix(self, out_file=False):
        if self.vocab is None:
            self.create_vocab()
        self.matrix = lil_matrix((len(self.vocab), len(self.vocab)), dtype='int')
        with open('knock82.100.txt', 'w') as f:
            for i, line in enumerate(open(self.filename)):
                if i % 1000 == 0:
                    print(i)
                words = line.lower().strip().split()
                for index in range(len(words)):
                    t = words[index]
                    if self.check_stop_word(words[index]):
                        continue

                    width = random.randint(1, 5)
                    left_context = words[index - width: index]
                    right_context = words[index + 1: index + width + 1]

                    for c in left_context + right_context:
                        if self.check_stop_word(c):
                            continue
                        self.matrix[self.vocab[t], self.vocab[c]] += 1

                    if out_file:
                        print(f'{t}\t{left_context + right_context}', file=f)

        self.dumps()

    def dumps(self):
        joblib.dump(self.matrix, 'matrix.pkl')
        joblib.dump(self.vocab, 'vocab.pkl')

    def check_stop_word(self, word):
        return True if self.vocab.get(word) is None else False


def main():
    matrix = Matrix()
    matrix.create_matrix(out_file=False)

    vocab = defaultdict(lambda: len(vocab))
    with open('knock82.100.txt', 'w') as f:
        for i, line in enumerate(open('knock81.100.txt')):
            if i % 1000 == 0:
                print(i)
            words = line.lower().strip().split()
            for index in range(len(words)):
                t = words[index]
                vocab[t]
                width = random.randint(1, 5)
                left_context = words[index - width: index]
                right_context = words[index + 1: index + width + 1]
                context = ' '.join(left_context + right_context)
                print(f'{t}\t{context}', file=f)


if __name__ == '__main__':
    main()

