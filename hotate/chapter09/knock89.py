import numpy as np
from sklearn.externals import joblib
from sklearn.metrics.pairwise import cosine_similarity


def main():
    pca = joblib.load('pca.pkl')
    vocab = joblib.load('vocab.pkl')
    words = list(vocab.keys())
    vec = pca[vocab['Spain'.lower()]] - pca[vocab['Madrid'.lower()]] + pca[vocab['Athens'.lower()]]
    top = [[0, 0] for i in range(10)]
    for index, t in enumerate(pca):
        if index % 10000 == 0:
            print(index)
        cs = cosine_similarity(np.reshape(vec, (1, -1)), np.reshape(t, (1, -1)))
        if cs > top[9][0]:
            top[9][0] = cs
            top[9][1] = words[index]
            top.sort()
            top.reverse()
    print(top)


if __name__ == '__main__':
    main()


"""
[array([[0.80340848]]), 'spain'], 
[array([[0.78173177]]), 'sweden'], 
[array([[0.75688807]]), 'italy'], 
[array([[0.72026164]]), 'germany'], 
[array([[0.71886927]]), 'austria'], 
[array([[0.70621056]]), 'norway'], 
[array([[0.70549223]]), 'belgium'], 
[array([[0.69901731]]), 'denmark'], 
[array([[0.68072742]]), 'france'], 
[array([[0.68006671]]), 'greece']]
"""