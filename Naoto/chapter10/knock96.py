'''
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
'''
import word2vec


def extract_vecs_of_countries():
    countries_path = "../chapter09/countries.txt"
    model = word2vec.load('out90.bin')

    res, labels = [], []
    with open(countries_path) as f_in:
        for name in map(lambda x: x.rstrip(), f_in):
            name = name.replace(' ', '_')
            try:
                res.append(model[name])
                labels.append(name)
            except:
                pass
    return res, labels


if __name__ == '__main__':
    vecs, countries = extract_vecs_of_countries()
    i = 0
    for i, (country, vec) in enumerate(zip(countries, vecs)):
        print(country)
        print(vec[:12], end='\n\n')
