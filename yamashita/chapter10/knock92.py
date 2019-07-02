from sklearn.externals import joblib
from gensim.models import word2vec, KeyedVectors
import numpy as np
from tqdm import tqdm


def cos_sim(v1, v2):
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.dot(v1, v2) / norm if norm else -1


def all_cos_sim(v, x_pca, index):
    dic = {}
    for key, value in index.items():
        sim = cos_sim(v, x_pca[value])
        dic[f'{key}'] = sim
    return sorted(dic.items(), key=lambda x: x[1], reverse=True)[0]


def main():
    X_PCA = joblib.load('../chapter9/X_PCA')
    t_index = joblib.load('../chapter9/t_index')
    wv = KeyedVectors.load('knock90.model')
    output_85 = 'result_knock92_85.txt'
    output_90 = 'result_knock92_90.txt'
    input_path = 'result_91.txt'

    with open(input_path, 'r', encoding='utf-8') as i_file, open(output_85, 'w', encoding='utf-8') as f_85, open(output_90, 'w', encoding='utf-8') as f_90:
        for line in tqdm(i_file):
            w1, w2, w3, _ = line.rstrip().split()
            try:
                vec_85 = X_PCA[t_index[w2]] - \
                    X_PCA[t_index[w1]] + X_PCA[t_index[w3]]
                sim_85 = all_cos_sim(vec_85, X_PCA, t_index)
                sim_w_85 = sim_85[0]
                sim_val_85 = sim_85[1]
            except:
                sim_w_85 = '-'
                sim_val_85 = '-'

            try:
                sim_90 = wv.most_similar(
                    positive=[w2, w3], negative=[w1], topn=1)
                sim_w_90 = sim_90[0][0]
                sim_val_90 = sim_90[0][1]
            except:
                sim_w_90 = '-'
                sim_val_90 = '-'
            print(f'{line.rstrip()} {sim_w_85} {sim_val_85}', file=f_85)
            print(f'{line.rstrip()} {sim_w_90} {sim_val_90}', file=f_90)


if __name__ == '__main__':
    main()


# ものすごく遅い 34m37s
