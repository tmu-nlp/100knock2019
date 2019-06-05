import joblib
import numpy as np
import faiss

def main():
    print("loading X_PCA...")
    X_pca = joblib.load("../chapter09/X_PCA")
    t_index  =joblib.load("../chapter09/t_index")
    faiss_pca = faiss.IndexFlatIP(300)
    faiss_pca.add(X_pca.astype('float32'))

    print("loading word2vec...")
    word_vectors = joblib.load("word_vectors")
    word_index = joblib.load("word_index")
    faiss_w2v = faiss.IndexFlatIP(300)
    faiss_w2v.add(word_vectors.astype('float32'))
    with open("family.txt") as f, open("pca_family.txt", mode="w") as f_pca, open("w2v_family.txt", mode="w") as f_w2v:
        for line in map(lambda x: x.rstrip(), f):
            word = [""] * 3
            word[0], word[1], word[2], *_ = line.split()
            try:
                # 類似ベクトル検索
                # 9章のベクトル
                v1 = X_pca[t_index[word[0]]]
                v2 = X_pca[t_index[word[1]]]
                v3 = X_pca[t_index[word[2]]]
                vec_pca  = v2 - v1 + v3
                sim_num = faiss_pca.search(np.array([vec_pca]).astype('float32'), 1)[1][0][0]
                pred_word = list(t_index.keys())[sim_num]
                f_pca.write(f"{word[0]} {word[1]} {word[2]} {pred_word}\n")
            except:
                f_pca.write(f"{word[0]} {word[1]} {word[2]} -\n")
            try:
                # word2vec
                v1 = word_vectors[word_index[word[0]]]
                v2 = word_vectors[word_index[word[1]]]
                v3 = word_vectors[word_index[word[2]]]
                vec_w2v = v2 - v1 + v3
                sim_num = faiss_w2v.search(np.array([vec_w2v]).astype('float32'), 1)[1][0][0]
                pred_word = list(word_index.keys())[sim_num]
                f_w2v.write(f"{word[0]} {word[1]} {word[2]} {pred_word}\n")
            except:
                f_w2v.write(f"{word[0]} {word[1]} {word[2]} -\n")

if __name__ == "__main__":
    main()