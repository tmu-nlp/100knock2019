from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from operator import itemgetter
import joblib

vocab = joblib.load('vocab')
matrix_300 = joblib.load('matrix_300') 

vec_England = matrix_300[vocab['England']].reshape(1, -1)

cos_sim_list = []
for i in range(len(vocab)):
    cos_sim = cosine_similarity(vec_England, matrix_300[i].reshape(1, -1))
    cos_sim_list.append(((i, cos_sim)))

cos_sim_list.sort(key=itemgetter(1), reverse=True)

for i, cos_sim in cos_sim_list[1:11]:
    word = [k for k, v in vocab.items() if v == i]
print(f'{i}\t{word}\t{cos_sim}')