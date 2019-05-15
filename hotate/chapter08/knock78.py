from sklearn.externals import joblib

from knock73 import Classifier


def main():
    vectorizer = joblib.load('vectorizer.pkl')
    label_list = joblib.load('label.pkl')
    sentence_list = joblib.load('sentences.pkl')
    logistic = joblib.load('model.pkl')
    model = Classifier(vectorizer=vectorizer, model=logistic, sentence_list=sentence_list, label_list=label_list)
    scores = model.kfold()
    for key, value in scores.items():
        print(f'{key} : {value.mean()}')


if __name__ == '__main__':
    main()
