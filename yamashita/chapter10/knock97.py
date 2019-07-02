from sklearn.externals import joblib
from gensim.models import word2vec, KeyedVectors
import numpy as np
from tqdm import tqdm
from scipy.stats import spearmanr
from sklearn.cluster import KMeans


def main():
    country_vecs = joblib.load('country_vecs')
    vecs = []
    keys = []
    for key, value in country_vecs.items():
        keys.append(key)
        vecs.append(value)

    kmeans = KMeans(n_clusters=5)
    model = kmeans.fit_predict(vecs)
    for key, cluster in zip(keys, model):
        print(f'{key}\t{cluster}')


if __name__ == '__main__':
    main()

# # India   3
# Republic_of_Indonesia   2
# Republic_of_Singapore   2
# Kingdom_of_Thailand     2
# Republic_of_Korea       2
# People's_Republic_of_China      0
# Japan   3
# Islamic_Republic_of_Pakistan    2
# People's_Republic_of_Bangladesh 2
# Republic_of_the_Philippines     2
# Brunei_Darussalam       2
# Malaysia        0
# Mongolia        0
# United_States_of_America        0
# Canada  3
# Argentine_Republic      2
# Antigua_and_Barbuda     2
# Grenada 2
# Jamaica 0
# Saint_Vincent_and_the_Grenadines        2
# Saint_Lucia     2
# Commonwealth_of_Dominica        2
# Dominican_Republic      0
# Republic_of_Panama      2
# Barbados        2
# Federative_Republic_of_Brazil   2
# Bolivarian_Republic_of_Venezuela        2
# Belize  2
# Republic_of_Peru        2
# Plurinational_State_of_Bolivia  2
# United_Mexican_States   2
# Ireland 1
# Republic_of_Azerbaijan  2
# Republic_of_Albania     2
# Republic_of_Armenia     2
# Principality_of_Andorra 2
# Italian_Republic        2
# Ukraine 0
# United_Kingdom_of_Great_Britain_and_Northern_Ireland    2
# Republic_of_Estonia     2
# Republic_of_Austria     2
# Kingdom_of_the_Netherlands      2
# Republic_of_Kazakhstan  2
# Republic_of_Cyprus      2
# Hellenic_Republic       2
# Republic_of_Croatia     2
# Republic_of_Kosovo      2
# Georgia 0
# Swiss_Confederation     2
# Kingdom_of_Sweden       2
# Spain   1
# Slovak_Republic 2
# Republic_of_Slovenia    2
# Republic_of_Serbia      2
# Republic_of_Tajikistan  2
# Czech_Republic  0
# Kingdom_of_Denmark      2
# Federal_Republic_of_Germany     2
# Turkmenistan    2
# Kingdom_of_Norway       2
# Vatican 2
# Hungary 1
# French_Republic 2
# Republic_of_Bulgaria    2
# Kingdom_of_Belgium      2
# Bosnia_and_Herzegovina  0
# Republic_of_Poland      2
# Portuguese_Republic     2
# Principality_of_Monaco  2
# Republic_of_Moldova     2
# Montenegro      0
# Romania 1
# Russian_Federation      2
# Commonwealth_of_Australia       2
# Cook_Islands    2
# Independent_State_of_Samoa      2
# Solomon_Islands 0
# Tuvalu  2
# Kingdom_of_Tonga        2
# Niue    2
# New_Zealand     3
# Republic_of_Fiji        2
# Federated_States_of_Micronesia  2
# Islamic_Republic_of_Afghanistan 2
# United_Arab_Emirates    2
# Republic_of_Yemen       2
# State_of_Israel 2
# Republic_of_Iraq        2
# Islamic_Republic_of_Iran        2
# Kingdom_of_Saudi_Arabia 2
# Republic_of_Turkey      2
# Kingdom_of_Bahrain      2
# Hashemite_Kingdom_of_Jordan     2
# Republic_of_Angola      2
# Arab_Republic_of_Egypt  2
# Republic_of_Ghana       2
# Republic_of_Kenya       2
# Republic_of_Congo       2
# Democratic_Republic_of_the_Congo        2
# Republic_of_Djibouti    2
# Republic_of_Zimbabwe    2
# Republic_of_Seychelles  2
# Central_African_Republic        2
# Federal_Republic_of_Nigeria     2
# Republic_of_Niger       2
# Burkina_Faso    2
# Republic_of_Botswana    2
# Republic_of_South_Africa        2
# Republic_of_Mozambique  2
# Kingdom_of_Morocco      2
# Libya   0
# United_States   4
# Isle_of_Man     2
