from sklearn.externals import joblib
from gensim.models import word2vec, KeyedVectors
import numpy as np
from tqdm import tqdm
from scipy.stats import spearmanr


def main():
    result_94_85 = 'result_knock94_85.txt'
    result_94_90 = 'result_knock94_90.txt'

    human_85 = []
    machine_85 = []
    with open(result_94_85, 'r', encoding='utf-8') as f_85:
        next(f_85)
        for line in f_85:
            values_85 = line.rstrip().split()
            h_85 = float(values_85[2])
            m_85 = 0 if values_85[3] == '-' else float(values_85[3])
            human_85.append(h_85)
            machine_85.append(m_85)

    human_90 = []
    machine_90 = []
    with open(result_94_90, 'r', encoding='utf-8') as f_90:
        next(f_90)
        for line in f_90:
            values_90 = line.rstrip().split()
            h_90 = float(values_90[2])
            m_90 = 0 if values_90[3] == '-' else float(values_90[3])
            human_90.append(h_90)
            machine_90.append(m_90)

    print(f'85 spearman : {spearmanr(human_85,machine_85).correlation}')
    print(f'90 spearman : {spearmanr(human_90,machine_90).correlation}')


if __name__ == '__main__':
    main()


# 85 spearman : 0.14088254385299756
# 90 spearman : 0.5092177567720028
