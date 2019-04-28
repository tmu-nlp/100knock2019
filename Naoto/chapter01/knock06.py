str1 = 'paraparaparadise'
str2 = 'paragraph'

import knock05

# def make_ngram(arr: [], n: int):
#    return list(arr[i:i + n] for i in range(len(arr) + 1 - n))

def nlp06():
    x = set(knock05.make_ngram(str1, 2))
    y = set(knock05.make_ngram(str2, 2))
    print(sorted(x.union(y)))
    print(sorted(x.difference(y)))
    print(sorted(x.intersection(y)))
    X = "se" in x
    Y = "se" in y
    print("seが'{0}'に含まれているか: {1}".format(str1, X))
    print("seが'{0}'に含まれているか: {1}".format(str2, Y))
    print("se" in x)
    print("se" in y)


nlp06()
