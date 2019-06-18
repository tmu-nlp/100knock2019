# 76. ラベル付け
# 学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
from sklearn.externals import joblib


def main():
    model = joblib.load('model')
    feature = joblib.load('feature')
    labels = joblib.load('sentiment')

    predicts = model.predict(feature)
    probs = model.predict_proba(feature)

    with open('lables.txt', 'w+', encoding='utf-8') as fout:
        for lbl, prd, prob in zip(labels, predicts, probs):
            print(lbl, prd, max(prob), sep='\t', file=fout)


if __name__ == '__main__':
    main()
