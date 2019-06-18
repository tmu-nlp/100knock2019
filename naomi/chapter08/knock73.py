# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib


def train(inpath: str, outpath: str):
    feature = joblib.load('feature')
    sentiment = joblib.load('sentiment')

    model = LogisticRegression().fit(feature, sentiment)

    joblib.dump(model, 'model')


def main():
    inputfile = 'sentiment.txt'
    outfile = 'lgisticmodel.txt'
    train(inputfile, outfile)


if __name__ == '__main__':
    main()
