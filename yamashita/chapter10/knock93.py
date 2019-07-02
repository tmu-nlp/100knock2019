from sklearn.externals import joblib
from gensim.models import word2vec, KeyedVectors
import numpy as np


def main():
    result_92_85 = 'result_knock92_85.txt'
    result_92_90 = 'result_knock92_90.txt'

    len_85 = 0
    correct_85 = 0
    with open(result_92_85, 'r', encoding='utf-8') as i_file:
        for line in i_file:
            values = line.rstrip().split()
            len_85 += 1
            if values[3] == values[4]:
                correct_85 += 1
        accuracy_85 = correct_85 / len_85

    len_90 = 0
    correct_90 = 0
    with open(result_92_90, 'r', encoding='utf-8') as i_file:
        for line in i_file:
            values = line.rstrip().split()
            len_90 += 1
            if values[3] == values[4]:
                correct_90 += 1
        accuracy_90 = correct_90 / len_90

    print(f'85 accuracy : {accuracy_85}')
    print(f'90 accuracy : {accuracy_90}')


if __name__ == '__main__':
    main()


# 85 accuracy : 0.019762845849802372
# 90 accuracy : 0.43873517786561267
