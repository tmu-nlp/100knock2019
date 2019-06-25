from tqdm import tqdm
import joblib
from scipy.sparse import lil_matrix

N = 0 
vocab = joblib.load('./vocab')
vocab_size = len(vocab)
matrix = lil_matrix((vocab_size, vocab_size))

# 行: 単語t 列: 文脈語c
for word_context in tqdm(open('./chapter09/context.txt', 'r').readlines()):
    word, context = word_context.rstrip('\n').split('\t')
    idx_t = vocab[word]
    idx_c = vocab[context]
    matrix[idx_t, idx_c] += 1
    N += 1

print(f'単語と文脈語のペアの総出現回数: {N}')
joblib.dump(matrix, 'matrix')