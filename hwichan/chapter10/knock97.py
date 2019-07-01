from scipy import io
import pickle
from sklearn.cluster import KMeans


def main():
    with open('./pickles/country_dict', 'rb') as f:
        country_dict = pickle.load(f)

    country_matrix = io.loadmat('country_matrix')['country_matrix']

    kmeans = KMeans(n_clusters=5).fit_predict(country_matrix)

    # coutry_dictはOrderdictで作ったからcountry_matrixの行と同じ順
    result = sorted(zip(kmeans, country_dict.keys()))
    for kmean, country in result:
        print(kmean, country)


if __name__ == '__main__':
    main()


