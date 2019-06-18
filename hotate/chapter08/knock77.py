from sklearn.externals import joblib
from sklearn.metrics import classification_report, accuracy_score

from knock73 import Classifier


def main():
    vectorizer = joblib.load('vectorizer.pkl')
    label_list = joblib.load('label.pkl')
    sentence_list = joblib.load('sentences.pkl')
    logistic = joblib.load('model.pkl')
    model = Classifier(vectorizer=vectorizer, model=logistic, sentence_list=sentence_list, label_list=label_list)
    label_true, label_pred = model.accuracy()
    print(classification_report(label_true, label_pred))
    print(f'accuracy = {accuracy_score(label_true, label_pred)}')


if __name__ == '__main__':
    main()
