from scipy import io
import pickle
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt


def main():
    with open('./pickles/country_dict', 'rb') as f:
        country_dict = pickle.load(f)

    country_matrix = io.loadmat('country_matrix')['country_matrix']

    w = ward(country_matrix)
    '''
        idx1        idx2   　　　　idx1,idx2の距離の和   データ数
        [[17.          47.           0.39823195   　　　　　2.]
         [3.           50.           0.4186454    　　　　　2.]
                        .
                        .
                        .
         ]
    '''

    dendrogram(w, labels=list(country_dict.keys()))
    plt.show()


if __name__ == '__main__':
    main()


