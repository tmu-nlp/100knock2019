from sklearn.externals import joblib
from sklearn import decomposition

matrix_ppmi = joblib.load('matrix_ppmi')
svd = decomposition.TruncatedSVD(300)
matrix_300 = svd.fit_transform(matrix_ppmi)
joblib.dump(matrix_300, 'matrix_300')