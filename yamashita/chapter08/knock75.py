from sklearn.externals import joblib


def main():
    model = joblib.load('model')
    weight = model.coef_[0].tolist()
    name = joblib.load('name')

    pair = list(zip(weight, name))
    pair.sort()

    print('重みの低い素性トップ10')
    for p in pair[:10]:
        print(f'{p[1]}\t{p[0]}')

    print('重みの高い素性トップ10')
    for p in pair[:-11:-1]:
        print(f'{p[1]}\t{p[0]}')


if __name__ == '__main__':
    main()
