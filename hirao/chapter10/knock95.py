import numpy as np
from scipy.stats import spearmanr

def main():
    with open("combined.csv") as f, open("knock94_pca.csv") as f_pca, open("knock94_w2v.csv") as f_w2v:
        next(f)
        scores = []
        for line in f:
            score = float(line.rstrip().split(",")[-1])
            scores.append(score)
        answer = np.array(scores)

        pca_scores = []
        for line in f_pca:
            score = float(line.rstrip().split(",")[-1])
            pca_scores.append(score)
        spear = spearmanr(answer, np.array(pca_scores))
        print(f"PCA      Data {spear}")

        w2v_scores = []
        for line in f_w2v:
            score = float(line.rstrip().split(",")[-1])
            w2v_scores.append(score)
        spear = spearmanr(answer, np.array(w2v_scores))
        print(f"Word2Vec Data {spear}")

if __name__ == "__main__":
    main()