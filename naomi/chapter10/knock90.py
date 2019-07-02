# 90. word2vecによる学習
# 81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
# さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．

import numpy as np
from gensim.models import word2vec
import logging

def cos_sim(wv1, wv2):
    norm = np.linalg.norm(wv1) * np.linalg.norm(wv2)
    if norm != 0:
        return np.dot(wv1, wv2) / norm
    else:
        return -1


calc = False
if calc:
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO)

    sentences = word2vec.Text8Corpus('./knock81.txt')

    # size: word vectorの次元, 
    # min_count: これより頻度の低い単語は無視, 
    # window: 今の単語と予測される単語の、文内での最大距離
    model = word2vec.Word2Vec(sentences, size=200, min_count=20, window=15)
    model.save('./model/corpus.model')

model = word2vec.Word2Vec.load('./model/corpus.model')

# 86. 単語ベクトルの表示
# 85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
# ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
usvec = model.wv['United_States']
print('knock86:')
print(f'United_States: {usvec}')

# 87. 単語の類似度
# 85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
# ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．

usvec2 = model.wv['U.S']
print('knock87:')
print(f'cosign similarity: {cos_sim(usvec, usvec2)}')


# 88. 類似度の高い単語10件
# 85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．

results = model.wv.most_similar(positive=['England'])
print('knock88:')
for result in results:
    print(result)


# 89. 加法構成性によるアナロジー
# 85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
# そのベクトルと類似度の高い10語とその類似度を出力せよ．

vector = model.wv['Spain'] - model.wv['Madrid'] + model.wv['Athens']
results = model.wv.similar_by_vector(vector)
print('knock89:')
for result in results:
    print(result)