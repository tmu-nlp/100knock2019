# 74. 予測
# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．

from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from knock72 import clean_sentence


def test(sentence: str) -> (int, float):
    model = joblib.load('model')
    vocab = joblib.load('vocab')

    sentence = clean_sentence(sentence)
    
    vectorizer = TfidfVectorizer(vocabulary=vocab)
    feature_vec = vectorizer.fit_transform([sentence]).toarray()

    predict = model.predict(feature_vec)[0]
    probability = model.predict_proba(feature_vec)[0]

    return (predict, probability)

def main():
    predict, probab = test("a semi-autobiographical film that's so sloppily written and cast that you cannot believe anyone more central to the creation of bugsy than the caterer had anything to do with it .")
    predict, probab = test(". . . only bond can save us from the latest eccentric , super-wealthy megalomaniac bent on world domination and destruction . ")

    print(predict, probab)

if __name__ == '__main__':
    main()