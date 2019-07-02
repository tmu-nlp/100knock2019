from knock90 import load_word_2_vec
from sklearn.externals import joblib
import numpy as np
from tqdm import tqdm


def sim_w2v():
    model = load_word_2_vec('word2vec')
    with open('knock92.90.txt', 'w') as f:
        for line in open('knock91.txt', 'r'):
            l = line.strip().split()
            try:
                vec = model[l[1]] - model[l[0]] + model[l[2]]
                similar = model.most_similar(positive=[vec], topn=1)
            except KeyError:
                similar = [['-', '-']]
            print(f'{line.strip()} {similar[0][0]} {similar[0][1]}', file=f)


def cos_sim(v1, v2):
    sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return sim if sim else -1


def sim_85():
    matrix = joblib.load('../chapter09/pca.pkl')
    vocab = joblib.load('../chapter09/vocab.pkl')
    norm = np.linalg.norm(matrix, ord=2, axis=1)
    mat = matrix / norm[:, np.newaxis]
    id_to_word = list(vocab.keys())
    with open('knock92.85.1.txt', 'w') as f:
        for line in tqdm(open('knock91.txt', 'r')):
            l = line.strip().split()
            top = [None, 0]
            try:
                vec = matrix[vocab[l[1]]] - matrix[vocab[l[0]]] + matrix[vocab[l[2]]]
                for index, t in enumerate(matrix):
                    cs = np.dot(mat[index], vec / np.linalg.norm(vec, ord=2))
                    if cs > top[1]:
                        top[1] = cs
                        top[0] = id_to_word[index]
            except KeyError:
                top[0] = '-'
                top[1] = '-'
            print(f'{line.strip()} {top[0]} {top[1]}', file=f)


def main():
    sim_85()
    sim_w2v()


if __name__ == '__main__':
    main()
