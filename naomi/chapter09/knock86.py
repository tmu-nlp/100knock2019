# 85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
# ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．

from tqdm import tqdm
from sklearn.decomposition import PCA
from collections import defaultdict
import pickle
import seaborn
import numpy as np
import pandas as pd
from pandas import plotting as plt


def save(file_name, data):
    with open(f"./pickles/{file_name}", 'wb') as f_out:
        pickle.dump(data, f_out)


def load(file_name):
    with open(f"./pickles/{file_name}", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


if __name__ == "__main__":
    # import X (300dimension) and t
    X300 = load('X300')
    t = load('t')

    # set PCA with num of principal components = 300
    pca = PCA(n_components=300)

    # execute PCA
    X300 = pca.fit_transform(X)
    
    print(X300[t['United_States']])
