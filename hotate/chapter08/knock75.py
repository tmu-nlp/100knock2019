from sklearn.externals import joblib

from knock73 import Classifier


def main():
    vectorizer = joblib.load('vectorizer.pkl')
    label_list = joblib.load('label.pkl')
    sentence_list = joblib.load('sentences.pkl')
    logistic = joblib.load('model.pkl')
    model = Classifier(vectorizer=vectorizer, model=logistic, sentence_list=sentence_list, label_list=label_list)
    wight_pair = model.weight_rank()
    print(wight_pair[:10])
    print(wight_pair[:-11:-1])


if __name__ == '__main__':
    main()
