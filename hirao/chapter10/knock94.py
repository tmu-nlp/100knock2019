import joblib
import numpy as np
from operator import matmul

def cos_sim(v1, v2):
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return matmul(v1, v2) / norm if norm else -1

def main():
    print("loading X_PCA...")
    X_pca = joblib.load("../chapter09/X_PCA")
    t_index  =joblib.load("../chapter09/t_index")

    print("loading word2vec...")
    word_vectors = joblib.load("word_vectors")
    word_index = joblib.load("word_index")

    with open("combined.csv") as f, open("knock94_pca.csv", mode="w") as f_pca, open("knock94_w2v.csv", mode="w") as f_w2v:
        next(f)
        for line in map(lambda x: x.rstrip(), f):
            word1, word2, score = line.rstrip().split(",")
            try:
                # 類似ベクトル検索
                # 9章のベクトル
                vec1_pca = X_pca[t_index[word1]]
                vec2_pca = X_pca[t_index[word2]]
                sim = cos_sim(vec1_pca, vec2_pca)
                f_pca.write(f"{word1},{word2},{sim}\n")
            except:
                f_pca.write(f"{word1},{word2},-1\n")
            try:
                # word2vec
                vec1_w2v = word_vectors[word_index[word1]]
                vec2_w2v = word_vectors[word_index[word2]]
                sim = cos_sim(vec1_w2v, vec2_w2v)
                f_w2v.write(f"{word1},{word2},{sim}\n")
            except:
                f_w2v.write(f"{word1},{word2},-1\n")

if __name__ == "__main__":
    main()
