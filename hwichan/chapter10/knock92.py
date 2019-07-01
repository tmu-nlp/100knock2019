import numpy as np
import pickle
from scipy import io


def cos_similarity(vec1, vec2):
    vec_norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    if vec_norm == 0:  # vec_normが０の場合は計算できないためエラーが出る
        return -1
    else:
        return np.dot(vec1, vec2) / vec_norm


def main():
    # dict_file = './pickles/knock90_idx_t'
    dict_file = './pickles/t_dict'
    with open(dict_file, 'rb') as f:
        t_dict = pickle.load(f)

    # matrix_file = 'knock90_300'
    # matrix_name = 'knock90_300'
    matrix_file = 'knock_x300'
    matrix_name = 'x300'
    matrix = io.loadmat(matrix_file)[matrix_name]

    # out_file = 'family_cos92.txt'
    out_file = 'family_cos85.txt'
    with open('family.txt', 'r') as input_f, \
            open(out_file, 'w') as out_f:
        for i, line in enumerate(input_f):
            cols = line.split(' ')

            try:
                # t_dictに単語がない場合エラー
                vec = matrix[t_dict[cols[1]]] \
                      - matrix[t_dict[cols[0]]] \
                      + matrix[t_dict[cols[2]]]

                cos_similarities = []

                for word, index in t_dict.items():
                    vec2 = matrix[index]
                    cos_sim = cos_similarity(vec, vec2)
                    cos_similarities.append((cos_sim, word))

                cos_similarities = sorted(cos_similarities, reverse=True)
                word = cos_similarities[0][1]
                value = cos_similarities[0][0]

            except KeyError:
                # 単語がないためNoneを指定しコサイン類似度は−１
                word = 'None'
                value = -1

            print(f'{line.strip()} {value} {word}', file=out_f)
            print(f'{line.strip()} {value} {word}')


if __name__ == "__main__":
    main()
