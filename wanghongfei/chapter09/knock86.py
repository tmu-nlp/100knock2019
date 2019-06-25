from sklearn.externals import joblib

vocab = joblib.load('vocab')
matrix_300 = joblib.load('matrix_300') 

vec_United_States = matrix_300[vocab['United_States']]
print(vec_United_States)