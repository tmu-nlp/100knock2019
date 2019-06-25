from tqdm import tqdm
import joblib
from scipy.sparse import lil_matrix
import numpy as np
import math

vocab = joblib.load('./vocab')
vocab_size = len(vocab)

matrix = joblib.load('./matrix')
matrix_ppmi = lil_matrix((vocab_size, vocab_size))

index = (matrix >= 10).nonzero()
t_idx, c_idx = index[0], index[1]
freq_t = np.sum(matrix, axis=1)
freq_c = np.sum(matrix, axis=1).reshape(vocab_size, 1)
N = np.sum(matrix)

for t, c in tqdm(zip(t_idx, c_idx)):
    ppmi = max(math.log((N * matrix[t, c]) / (freq_t[t] * freq_c[c])), 0) 
    matrix_ppmi[t, c] = ppmi

joblib.dump(matrix_ppmi, 'matrix_ppmi')