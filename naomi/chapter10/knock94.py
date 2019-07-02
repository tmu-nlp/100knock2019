# 94. WordSimilarity-353での類似度計算
# The WordSimilarity-353 Test Collectionの評価データを入力とし，1列目と2列目の単語の類似度を計算し，
# 各行の末尾に類似度の値を追加するプログラムを作成せよ．
# このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．

import numpy as np
from gensim.models import word2vec


def cos_sim(wv1, wv2):
    norm = np.linalg.norm(wv1) * np.linalg.norm(wv2)
    if norm != 0:
        return np.dot(wv1, wv2) / norm
    else:
        return -1


model = word2vec.Word2Vec.load('./model/corpus.model')

with open('./out94.py', 'w+', encoding='utf-8') as fo:
    with open('./wordsim353/combined.tab', 'r', encoding='utf-8') as fin:
        next(fin)
        for line in fin:
            word1, word2, n = line.rstrip().split()
            if word1 in model.wv.vocab and word2 in model.wv.vocab:
                wv1 = model.wv[word1]
                wv2 = model.wv[word2]
                sim = cos_sim(wv1, wv2)
                print(f'{word1}\t{word2}\t{n}\t{sim}', file=fo)
