from sklearn.externals import joblib


def main():
    matrix = joblib.load('matrix.pkl')
    vocab = joblib.load('vocab.pkl')

    while True:
        t = input('t: ')
        c = input('c: ')

        N = matrix.sum()

        # count_tc = matrix[vocab[t], vocab[c]]
        # count_t = matrix[vocab[t], :].sum()
        # count_c = matrix[:, vocab[c]]

        try:
            count_tc = matrix[vocab[t], vocab[c]]
            count_t = matrix[vocab[t], :].sum()
            count_c = matrix[:, vocab[c]]

            print(f'f(t, c): {count_tc}')
            print(f'f(t, *): {count_t}')
            print(f'f(*, c): {count_c}')
            print(f'N: {N}')
        except KeyError:
            print('Out of vocabulary.')
            continue


if __name__ == '__main__':
    main()
