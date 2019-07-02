import pickle
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import ward, dendrogram



data_path = './chapter10/country_vec'
with open(data_path, 'rb') as f:
        country_index = pickle.load(f)
        vec = pickle.load(f)
Z = ward(vec)
plt.figure()
dendrogram(Z, labels=list(country_index.values()))
plt.show()