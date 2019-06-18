from sklearn.externals import joblib


def main():
    model = joblib.load('model')
    sentiment = joblib.load('sentiment')
    feature = joblib.load('feature')

    predict = model.predict(feature)
    probability = model.predict_proba(feature)

    with open('result_knock76.txt', 'w', encoding='utf-8') as w_file:
        for label, pre, prob in zip(sentiment, predict, probability):
            print(f'{label}\t{pre}\t{max(prob)}', file=w_file)


if __name__ == '__main__':
    main()
