from knock90 import load_word_2_vec
from sklearn.externals import joblib
import numpy as np
from tqdm import tqdm


def calc_w2v(model):
    with open('knock94_90.txt', 'w') as f:
        for line in open('combined.tab', 'r'):
            l = line.strip().split()
            try:
                similar = model.similarity(l[0], l[1])
            except KeyError:
                similar = -1
            print(f'{line.strip()} {similar}', file=f)


def calc_85():
    matrix = joblib.load('../chapter09/pca.pkl')
    vocab = joblib.load('../chapter09/vocab.pkl')
    norm = np.linalg.norm(matrix, ord=2, axis=1)
    matrix = matrix / norm[:, np.newaxis]
    with open('knock94_85.txt', 'w') as f:
        for line in tqdm(open('combined.tab', 'r')):
            l = line.strip().split()
            try:
                cs = np.dot(matrix[vocab[l[0]]], matrix[vocab[l[1]]])
            except KeyError:
                cs = -1
            print(f'{line.strip()} {cs}', file=f)


if __name__ == '__main__':
    calc_85()
    model = load_word_2_vec('word2vec')
    calc_w2v(model)
