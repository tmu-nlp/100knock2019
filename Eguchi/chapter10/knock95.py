"""
94で作ったデータを用い，各モデルが出力する類似度のランキングと，人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""

import numpy as np

in_fn1 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter10\combined_out_85.tab"
in_fn2 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter10\combined_out_90.tab"


def cul (in_f):


    with open(in_f,"rt" ) as f:
        e_score =[]
        h_score = []
        Counter=0
        N = 0

        for line in f:
            scores = line.split("\t")
            e_score.append(scores[2])
            h_score.append(scores[3])
            N +=1
        
        e_score_sorted = np.argsort(e_score)
        h_score_sorted = np.argsort(h_score)

        e_order = [0] * N
        h_order = [0] * N

        for i in range(N):
            e_order[e_score_sorted[i]] = i
            h_order[h_score_sorted[i]] = i
        
        total = 0
        for i in range(N):
            total += pow(h_order[i] - e_order[i], 2)
        
        ans = 1 - (6 * total ) / (pow(N, 3)- N)

        print(ans)

cul(in_fn1)
cul(in_fn2)