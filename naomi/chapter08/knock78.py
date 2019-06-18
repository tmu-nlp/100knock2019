# 78. 5分割交差検定
# 76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
# すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，
# モデルの汎化性能を測定していない．
# そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
from sklearn.externals import joblib
from sklearn.model_selection import cross_validate
from statistics import mean


def main():
    model = joblib.load('model')
    feature = joblib.load('feature')
    labels = joblib.load('sentiment')

    scr = ['accuracy', 'precision', 'recall', 'f1']
    result = cross_validate(model, feature, labels, cv=5, scoring=scr)

    accuracy = mean(result['test_accuracy'])
    print(f'Accuracy: {accuracy}')

    precision = mean(result['test_precision'])
    print(f'Precision: {precision}')

    recall = mean(result['test_recall'])
    print(f'Recall: {recall}')

    f1 = mean(result['test_f1'])
    print(f'F1: {f1}')


if __name__ == '__main__':
    main()
