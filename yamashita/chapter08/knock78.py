from sklearn.externals import joblib
from sklearn.model_selection import cross_validate
from statistics import mean


def main():
    model = joblib.load('model')
    sentiment = joblib.load('sentiment')
    feature = joblib.load('feature')

    scoring = ['accuracy', 'precision', 'recall', 'f1']
    result = cross_validate(model, feature, sentiment, cv=5, scoring=scoring)
    print(f'正答率：{mean(result["test_accuracy"])}')
    print(f'適合率：{mean(result["test_precision"])}')
    print(f'再現率：{mean(result["test_recall"])}')
    print(f'F1スコア：{mean(result["test_f1"])}')


if __name__ == '__main__':
    main()
