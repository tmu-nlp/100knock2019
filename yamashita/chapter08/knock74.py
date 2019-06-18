from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from knock72 import get_feature_base
# from tqdm import tqdm


def main():
    skip_num = 100
    num = 5
    model = joblib.load('model')
    vocab = joblib.load('vocabulary')

    with open('sentiment.txt', 'r', encoding='utf-8') as i_file:
        for _ in range(skip_num):
            next(i_file)
        for i in range(num):
            sentence = i_file.readline()
            print(f'入力{i} : {sentence.strip()[3:]}')
            feature = get_feature_base(sentence)
            vectorizer = TfidfVectorizer(vocabulary=vocab)
            feature_vec = vectorizer.fit_transform([feature]).toarray()

            predict = model.predict(feature_vec)[0]
            probability = model.predict_proba(feature_vec)[0]

            if predict == -1:
                print(f'negative {probability[0] * 100:.6f}%')
            else:
                print(f'positive {probability[1] * 100:.6f}%')


if __name__ == '__main__':
    main()
