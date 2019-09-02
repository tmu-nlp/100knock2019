'''
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
'''


from sys import argv
import numpy as np
from gensim.models import word2vec
import logging


def cos_sim(a, b):
    dot = np.dot(a, b)
    if dot == 0:
        return -1
    return dot / np.linalg.norm(a) / np.linalg.norm(b)


sentences = word2vec.Text8Corpus('../chapter09/out81.txt')
if argv[1:] != ["load"]:
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = word2vec.Word2Vec(sentences, size=300, min_count=5, window=5)
    model.save("word2vec_model")
else:
    print("loading")
    model = word2vec.Word2Vec.load("word2vec_model")
    print("loaded")
    print()

print(model.__dict__['wv']['United_States'][:12])  # knock86
print()
print(cos_sim(model.__dict__['wv']['United_States'], model.__dict__['wv']['U.S']))  # knock87
print()

ret = model.wv.most_similar(positive=['England'])  # knock88
for item in ret:
    print(item[0], item[1])
print()

vec = model.__dict__['wv']['Spain'] - model.__dict__['wv']['Madrid'] + model.__dict__['wv']['Athens']  # knock89
ret = model.wv.most_similar([vec])
for item in ret:
    print(item[0], item[1])


'''
https://qiita.com/makaishi2/items/63b7986f6da93dc55edd word2vec の使い方

https://qiita.com/iss-f/items/aec567ee5c79464413dc  model.most_similar の使い方
'''

'''
実行結果

[ 0.66119236 -0.8832757   1.0976988   0.16715096 -0.40276572 -0.67977494
 -0.33983737  0.2894182  -1.4614888  -1.3918911  -0.33725202 -0.42468387]

0.85911

2019-09-01 11:12:19,540 : INFO : precomputing L2-norms of word weight vectors
Scotland 0.8038942217826843
Wales 0.733869194984436
Ireland 0.6385107040405273
London 0.59712815284729
Lancashire 0.5849387049674988
Britain 0.5787779092788696
Plymouth 0.5748987793922424
Sweden 0.5642446279525757
Spain 0.5609540939331055
Liverpool 0.5599052906036377

Spain 0.8994535207748413
Italy 0.8286198377609253
Denmark 0.7966439723968506
Austria 0.7937094569206238
Egypt 0.78947913646698
Russia 0.7781189680099487
Sweden 0.7779057025909424
Greece 0.7615749835968018
Portugal 0.7542418837547302
Poland 0.7506155967712402

'''
