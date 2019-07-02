# 92. アナロジーデータへの適用
# 91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
# そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
# 求めた単語と類似度は，各事例の末尾に追記せよ．このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
import numpy as np
from gensim.models import word2vec


def cos_sim(wv1, wv2):
    norm = np.linalg.norm(wv1) * np.linalg.norm(wv2)
    if norm != 0:
        return np.dot(wv1, wv2) / norm
    else:
        return -1


model = word2vec.Word2Vec.load('./model/corpus.model')

with open('out92.txt', 'w+', encoding='utf-8') as f:
    for line in open('family.txt', 'r', encoding='utf-8'):

        word1, word2, word3, word4 = line.rstrip().split()

        if word1 in model.wv.vocab and word2 in model.wv.vocab and \
           word3 in model.wv.vocab:
            wv1 = model.wv[word1]
            wv2 = model.wv[word2]
            wv3 = model.wv[word3]

            vector = wv2 - wv1 + wv3
            result = model.wv.similar_by_vector(vector, topn=1)
            print(f'{word1} {word2} {word3} {word4} {result[0][0]} {result[0][1]}', file=f)
        # else:
        #     print(f'{word1} {word2} {word3} {word4}', file=f)
