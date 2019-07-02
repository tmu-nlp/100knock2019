# 96. 国名に関するベクトルの抽出
# word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．

import numpy as np
from gensim.models import word2vec
import yaml
import dill


def cos_sim(wv1, wv2):
    norm = np.linalg.norm(wv1) * np.linalg.norm(wv2)
    if norm != 0:
        return np.dot(wv1, wv2) / norm
    else:
        return -1


def save(file_name, data):
    with open(f"./dills/{file_name}", 'wb') as f_out:
        dill.dump(data, f_out)


def load(file_name):
    with open(f"./dills/{file_name}", 'rb') as f_in:
        data = dill.load(f_in)
    return data


model = word2vec.Word2Vec.load('./model/corpus.model')

json_path = "./country-json/src/country-by-name.json"

countries = []
vectors = []
with open(json_path) as json_file:
    for name in map(lambda x: x['country'], yaml.safe_load(json_file)):
        if ' ' in name:
            name = name.replace(' ', '_')
        if name in model.wv.vocab:
            countries.append(name)
            vectors.append(model.wv[name])
save('countries', countries)
save('X', vectors)
