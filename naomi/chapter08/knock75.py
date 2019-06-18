# 75. 素性の重み
# 73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．

from sklearn.externals import joblib


def main():
    model = joblib.load('model')
    name = joblib.load('name')

    coef = model.coef_[0].tolist()

    # タプルのリストとしてまとめる
    weights = list(zip(coef, name))

    weights.sort()

    for w in weights[:10]:
        print(f'{w[1]}\t{w[0]}')

    for w in weights[:-11:-1]:
        print(f'{w[1]}\t{w[0]}')


if __name__ == '__main__':
    main()
