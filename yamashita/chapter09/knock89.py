from sklearn.decomposition import TruncatedSVD
from sklearn.externals import joblib
import numpy as np


def cos_sim(v1, v2):
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.dot(v1, v2) / norm if norm else -1


def main():
    X_PCA = joblib.load('X_PCA')
    t_index = joblib.load('t_index')

    vec = X_PCA[t_index['Spain']] - \
        X_PCA[t_index['Madrid']] + X_PCA[t_index['Athens']]

    sim_dic = {}
    for key, value in t_index.items():
        sim = cos_sim(vec, X_PCA[value])
        sim_dic[f'{key}'] = sim

    for key, value in sorted(sim_dic.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f'{key}\t{value}')


if __name__ == '__main__':
    main()


# Macedonians     0.7836705089082521
# Greece  0.762089972862676
# Istanbul        0.7477052279911404
# Turkey  0.7357647898115637
# Austria 0.7281099263293452
# Belgium 0.7247743437084446
# Netherlands     0.7233839909372439
# Brest   0.7205267220253787
# visited 0.7184059012440481
# Sweden  0.7169250000055362
