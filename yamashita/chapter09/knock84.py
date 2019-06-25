from tqdm import tqdm
from sklearn.externals import joblib
from scipy.sparse import lil_matrix
import math


def main():
    print('start loading')
    count_tc = joblib.load('count_tc')
    print('tc finish')
    count_t = joblib.load('count_t')
    print('t finish')
    count_c = joblib.load('count_c')
    print('c finish')
    n_count = joblib.load('n_count')
    print('finish loading')

    t_index = {key: i for i, key in enumerate(count_t.keys())}
    c_index = {key: i for i, key in enumerate(count_c.keys())}
    joblib.dump(t_index, 't_index')
    joblib.dump(c_index, 'c_index')

    X = lil_matrix((len(count_t), len(count_c)))

    for tc, counts in tqdm(count_tc.items()):
        if counts < 10:
            continue
        t, c = tc.split('\t')
        ppmi = max(0, math.log2(n_count * counts / count_t[t] / count_c[c]))
        if ppmi == 0:
            continue
        X[t_index[t], c_index[c]] = ppmi
    X = X.tocsr()
    joblib.dump(X, 'X_tc', compress=True)
    print('Finish')


if __name__ == '__main__':
    main()
