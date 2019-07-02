import pickle
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans


vec_file = './chapter10/country_vec'
with open(vec_file, 'rb') as f:
        country_index = pickle.load(f)
        vec = pickle.load(f)
        cls = KMeans(5).fit(vec)
        for i, label in enumerate(cls.labels_):
            print(label, country_index[i])