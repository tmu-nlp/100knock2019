"""
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""

from scipy.stats import spearmanr
import numpy as np


def spearman(filename: str, name: str):
    manual, model = [], []
    for line in open(filename, "r", encoding="utf-8"):
        res = line.rstrip().split()
        if "-" in res:
            continue

        manual.append(float(res[2]))
        model.append(float(res[3]))

    manual, model = np.array(manual), np.array(model)
    print(f"{name.ljust(10)} : {spearmanr(manual, model)[0]:.4f}")


spearman("./results/knock94.ppmi.txt", "PPMI")
spearman("./results/knock94.w2v.txt", "word2vec")
