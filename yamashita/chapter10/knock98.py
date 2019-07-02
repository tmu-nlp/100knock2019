from sklearn.externals import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


def main():
    country_vecs = joblib.load('country_vecs')

    df = pd.DataFrame(country_vecs.values(), index=country_vecs.keys())
    result = linkage(df, method='ward', metric='euclidean')

    dendrogram(result, labels=list(country_vecs.keys()), leaf_font_size=6)
    plt.show()


if __name__ == '__main__':
    main()
