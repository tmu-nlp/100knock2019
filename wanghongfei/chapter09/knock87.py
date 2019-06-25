from sklearn.metrics.pairwise import cosine_similarity
import joblib

vocab = joblib.load('vocab')
matrix_300 = joblib.load('matrix_300') 

vec_United_States = matrix_300[vocab['United_States']].reshape(1, -1)
vec_US = matrix_300[vocab['U.S']].reshape(1, -1)

cos_sim = cosine_similarity(vec_United_States, vec_US)

print(cos_sim)