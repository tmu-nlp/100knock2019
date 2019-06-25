from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from operator import itemgetter
import joblib

matrix_300 = joblib.load('matrix_300') 
vocab = joblib.load('vocab')

vec_Spain = matrix_300[vocab['Spain']].reshape(1, -1)
vec_Madrid = matrix_300[vocab['Madrid']].reshape(1, -1)
vec_Athens = matrix_300[vocab['Athens']].reshape(1, -1)

vec = vec_Spain - vec_Madrid + vec_Athens

cos_sim_list = []
for i in range(len(vocab)):
    cos_sim = cosine_similarity(vec, matrix_300[i].reshape(1, -1))
    cos_sim_list.append(((i, cos_sim)))

cos_sim_list.sort(key=itemgetter(1), reverse=True)

for i, cos_sim in cos_sim_list[1:11]:
    word = [k for k, v in vocab.items() if v == i]
print(f'{i}\t{word}\t{cos_sim}')