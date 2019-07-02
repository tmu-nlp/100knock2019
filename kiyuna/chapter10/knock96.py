'''
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
'''
import yaml
import word2vec


def extract_vecs_of_countries():
    json_path = "../chapter09/country-json/src/country-by-name.json"
    model = word2vec.load('out90.bin')

    res, labels = [], []
    with open(json_path) as json_file:
        for name in map(lambda x: x['country'], yaml.safe_load(json_file)):
            name = name.replace(' ', '_')
            try:
                res.append(model[name])
                labels.append(name)
            except Exception as e:
                pass
    return res, labels


if __name__ == '__main__':
    extract_vecs_of_countries()
