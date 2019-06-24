from sklearn.externals import joblib
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def main():
    pca = joblib.load('pca.pkl')
    vocab = joblib.load('vocab.pkl')
    words = list(vocab.keys())
    england = pca[vocab['England'.lower()]]
    eng_num = vocab['England'.lower()]
    top = [[0, 0] for _ in range(10)]
    for index, t in enumerate(pca):
        if index % 10000 == 0:
            print(index)
        cs = cosine_similarity(np.reshape(england, (1, -1)), np.reshape(t, (1, -1)))
        if cs > top[9][0] and index != eng_num:
            top[9][0] = cs
            top[9][1] = words[index]
            top.sort()
            top.reverse()
    print(top)


if __name__ == '__main__':
    main()

"""
[[array([[0.69387815]]), 'scotland'], 
[array([[0.62489658]]), 'wales'], 
[array([[0.62292187]]), 'australia'], 
[array([[0.57711498]]), 'ireland'], 
[array([[0.57432217]]), 'france'], 
[array([[0.5490898]]), 'italy'], 
[array([[0.54153971]]), 'spain'], 
[array([[0.53495091]]), 'germany'], 
[array([[0.53355223]]), 'united_kingdom'], 
[array([[0.51871539]]), 'cheshire']]
"""