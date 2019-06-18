'''
74. 予測
73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．
'''


from sklearn.feature_extraction.text import TfidfVectorizer
from knock73 import serialize, deserialize, labels_sentences


def prediction(path="prediction.txt", write=""):
    with open(path, "w", encoding="latin-1") as fw:
        model = deserialize("model")
        vocabs = deserialize("vocabs")
        _, sentences = labels_sentences()
        vectorizer = TfidfVectorizer(vocabulary=vocabs)
        features = vectorizer.fit_transform(sentences).toarray()
        predict = model.predict(features)
        probs = model.predict_proba(features)
        pp = zip(predict, probs)
        # for predict, probs in pp:
        #     fw.write(f"{predict} {max(probs):.6}\n")
    return pp


if __name__ == "__main__":
    prediction()
