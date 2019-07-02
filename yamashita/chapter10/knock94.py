from sklearn.externals import joblib
from gensim.models import word2vec, KeyedVectors
import numpy as np
from tqdm import tqdm


def cos_sim(v1, v2):
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.dot(v1, v2) / norm if norm else -1


def main():
    X_PCA = joblib.load('../chapter9/X_PCA')
    t_index = joblib.load('../chapter9/t_index')
    wv = KeyedVectors.load('knock90.model')
    output_85 = 'result_knock94_85.txt'
    output_90 = 'result_knock94_90.txt'
    input_path = 'wordsim353/combined.tab'

    with open(input_path, 'r', encoding='utf-8') as i_file, open(output_85, 'w', encoding='utf-8') as f_85, open(output_90, 'w', encoding='utf-8') as f_90:
        next(i_file)
        for line in tqdm(i_file):
            w1, w2, human = line.rstrip().split()
            try:
                sim_85 = cos_sim(X_PCA[t_index[w1]], X_PCA[t_index[w2]])
            except:
                sim_85 = '-'

            try:
                sim_90 = wv.similarity(w1, w2)
            except:
                sim_90 = '-'
            print(f'{line.rstrip()} {sim_85}', file=f_85)
            print(f'{line.rstrip()} {sim_90}', file=f_90)


if __name__ == '__main__':
    main()
