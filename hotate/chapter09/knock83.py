import os
from scipy.sparse import lil_matrix
from sklearn.externals import joblib


def create_matrix(vocab):
    matrix = lil_matrix((len(vocab), len(vocab)), dtype='int')

    for i, line in enumerate(open('knock82.100.txt', 'r')):
        if i % 1000 == 0:
            print(i)
        line = line.strip().split('\t')
        t = line[0]
        contexts = line[1]
        for c in contexts.split():
            matrix[vocab[t], vocab[c]] += 1

    joblib.dump(matrix, 'matrix.pkl')


def main():
    vocab = joblib.load('vocab.pkl')
    if not os.path.isfile('matrix.pkl'):
        create_matrix(vocab)
    matrix = joblib.load('matrix.pkl')
    while True:
        t = input('t: ').lower()
        c = input('c: ').lower()

        N = matrix.sum()

        try:
            count_tc = matrix[vocab[t], vocab[c]]
            count_t = matrix[vocab[t], :].sum()
            count_c = matrix[:, vocab[c]]

            print(f'f(t, c): {count_tc}')
            print(f'f(t, *): {count_t}')
            print(f'f(*, c): {count_c}')
            print(f'N: {N}')
        except KeyError:
            print('Out of vocabulary.')
            continue


if __name__ == '__main__':
    main()
