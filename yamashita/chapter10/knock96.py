from sklearn.externals import joblib
from gensim.models import word2vec, KeyedVectors
import numpy as np
from tqdm import tqdm
from scipy.stats import spearmanr


def main():
    wv = KeyedVectors.load('knock90.model')
    countries_txt = '../chapter9/countries.txt'

    countries = []
    with open(countries_txt, 'r', encoding='utf-8') as c_file:
        for line in c_file:
            country = '_'.join(line.rstrip().split())
            countries.append(country)

    country_vecs = {}
    for c_name in countries:
        try:
            vec = wv[c_name]
            country_vecs[c_name] = vec
        except:
            pass

    joblib.dump(country_vecs, 'country_vecs')


if __name__ == '__main__':
    main()
