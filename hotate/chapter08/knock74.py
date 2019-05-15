from sklearn.externals import joblib

from knock73 import Classifier


def main():
    vectorizer = joblib.load('vectorizer.pkl')
    label_list = joblib.load('label.pkl')
    sentence_list = joblib.load('sentences.pkl')
    logistic = joblib.load('model.pkl')
    model = Classifier(vectorizer=vectorizer, model=logistic, sentence_list=sentence_list, label_list=label_list)
    pred_set = model.predict()
    for sentence, pred, prob, gold in pred_set:
        print('-' * 100)
        print(f'入力文 : {sentence.strip()}')
        print(f'予測結果 : {pred}')
        print(f'予測確率 : {prob}')
        print()


if __name__ == '__main__':
    main()
