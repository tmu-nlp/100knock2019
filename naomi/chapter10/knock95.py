# 95. WordSimilarity-353での評価
# 94で作ったデータを用い，各モデルが出力する類似度のランキングと，
# 人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．

import numpy as np

hm_score = []
ml_score = []

for line in open('out94.txt', 'r', encoding='utf-8'):
    _, _, hm, ml = line.rstrip().split()
    hm_score.append(float(hm))
    ml_score.append(float(ml))

spearman = np.corrcoef(hm_score, ml_score)
print(spearman)
