from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib


def main():
    feature = joblib.load('feature')
    sentiment = joblib.load('sentiment')

    model = LogisticRegression(random_state=0).fit(feature, sentiment)

    joblib.dump(model, 'model')


if __name__ == '__main__':
    main()
