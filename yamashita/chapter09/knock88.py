from sklearn.decomposition import TruncatedSVD
from sklearn.externals import joblib
import numpy as np


def cos_sim(v1, v2):
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.dot(v1, v2) / norm if norm else -1


def main():
    X_PCA = joblib.load('X_PCA')
    t_index = joblib.load('t_index')

    England = X_PCA[t_index['England']]

    sim_dic = {}
    for key, value in t_index.items():
        sim = cos_sim(England, X_PCA[value])
        sim_dic[f'{key}'] = sim

    for key, value in sorted(sim_dic.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f'{key}\t{value}')


if __name__ == '__main__':
    main()


# England 1.0
# Cheshire        0.7105012345283026
# NWA     0.6078223316620682
# Wildside        0.5911266236178779
# Scotland        0.5444686811764462
# sailed  0.4960644685719889
# Patriots        0.4878888469654257
# Ireland 0.45351930165653803
# Wales   0.4469739071043
# Guinea  0.4319167015661852
