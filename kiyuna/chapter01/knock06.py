'''
06. 集合
"paraparaparadise" と "paragraph" に含まれる文字 bi-gram の集合を，
それぞれ, X と Y として求め，X と Y の和集合，積集合，差集合を求めよ．
さらに，'se' という bi-gram が X および Y に含まれるかどうかを調べよ．
'''
from knock05 import n_gram      # -B をつけるとキャッシュが出ない

if __name__ == '__main__':
    w1 = "paraparaparadise"
    w2 = "paragraph"
    tgt = n_gram('se', n=2).pop()

    X = set(n_gram(w1, n=2))
    Y = set(n_gram(w2, n=2))

    print('X =', X)
    print('Y =', Y)

    print('X ∪ Y = {}'.format(X | Y))  # X.union(Y)
    print('X ∩ Y = {}'.format(X & Y))  # X.intersection(Y)
    print('X \ Y = {}'.format(X - Y))  # X.difference(Y)
    print('Y \ X = {}'.format(Y - X))  # Y.difference(X)

    print(f"X includes 'se': {tgt in X}")
    print(f"Y includes 'se': {tgt in Y}")
