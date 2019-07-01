from knock92 import cos_similarity
import pickle
from scipy import io


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

    # out_file = 'combined_knock94.txt'
    out_file = 'combined_knock85.txt'
    with open('combined.tab', 'r') as input_f, \
            open(out_file, 'w') as out_f:

        for i, line in enumerate(input_f):
            # Word 1	Word 2	Human (mean)　各列の説明
            if i == 0:
                continue

            try:
                cols = line.strip().split('\t')
                cos_sim = cos_similarity(matrix[t_dict[cols[0]]], matrix[t_dict[cols[1]]])
                print(f'{line.strip()}\t{cos_sim}')
                print(f'{line.strip()}\t{cos_sim}', file=out_f)

            except KeyError:
                cos_sim = -1
                print(f'{line.strip()}\t{cos_sim}')
                print(f'{line.strip()}\t{cos_sim}', file=out_f)


if __name__ == "__main__":
    main()
