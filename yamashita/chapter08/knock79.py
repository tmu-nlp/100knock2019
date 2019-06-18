from sklearn.metrics import precision_recall_curve
from sklearn.externals import joblib
import matplotlib.pyplot as plt


def main():
    model = joblib.load('model')
    sentiment = joblib.load('sentiment')
    feature = joblib.load('feature')

    probability = model.predict_proba(feature)

    precision, recall, _ = precision_recall_curve(
        sentiment, probability[0:, 1])

    plt.plot(precision, recall)
    plt.xlabel('precision')
    plt.ylabel('recall')
    plt.show()


if __name__ == '__main__':
    main()
