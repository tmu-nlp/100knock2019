import numpy as np
from scipy import io
import pickle
from collections import OrderedDict


def main():
    dict_file = './pickles/knock90_idx_t'
    with open(dict_file, 'rb') as f:
        t_dict = pickle.load(f)

    matrix_file = 'knock90_300'
    matrix_name = 'knock90_300'
    matrix = io.loadmat(matrix_file)[matrix_name]

    country_dict = OrderedDict()
    country_matrix = np.empty([0, 300], dtype=np.float64)  # 0行300列の行列を用意

    with open('countries.txt', 'r') as f:
        for line in f:
            line = line.strip()
            try:
                country = line.replace(' ', '_')
                idx = t_dict[country]
                # np.vstach: 行列を結合
                country_matrix = np.vstack([country_matrix, matrix[idx]])
                country_dict[country] = len(country_dict)
            except KeyError:
                pass

    io.savemat('country_matrix', {'country_matrix': country_matrix})
    with open('./pickles/country_dict', 'wb') as f:
        pickle.dump(country_dict, f)


if __name__ == "__main__":
    main()
