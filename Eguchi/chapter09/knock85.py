# 84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ

from scipy import sparse, io
import sklearn.decomposition

fname_matrix_x = 'matrix_x'
fname_matrix_x_300 = 'matrix_x_300'

matrix_x = io.loadmat(fname_matrix_x)['matrix_x']

print(matrix_x)
clf = sklearn.decomposition.TruncatedSVD(300)
matrix_x_300 = clf.fit_transform(matrix_x)
io.savemat(fname_matrix_x_300, {'matrix_x_300': matrix_x_300})