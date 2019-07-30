#81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
from gensim.models import word2vec
import pickle
from collections import OrderedDict
import numpy as np
from scipy import io


f_input = 'corpus81.100.txt'
f_word2vec_out = 'vectors.txt'
f_dict_index_t = 'dict_index_t'
f_matrix_x_300 = 'matrix_x_300'

sentence = word2vec.LineSentence(f_input)
model = word2vec.Word2Vec(sentence,  size=300, min_count=4, window=5)

model.save(f_word2vec_out)

word2vec.Word2Vec.load(f_word2vec_out)

print("United_States_of_America")
print(model["United_States_of_America"])



print("similarity_U.S")
print(model.similarity(u'United_States_of_America', u'U.S'))


print("similarity_England")
print(model.most_similar(positive=['England'], topn=10))

mult = model["Spain"] - model["Madrid"] + model["Athens"]
print("spain - madrid + athene")
print(model.most_similar(positive=[mult], topn=10))

