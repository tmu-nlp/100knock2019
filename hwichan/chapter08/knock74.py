from knock73 import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def create_model():
    sentences = []
    labels = []
    with open('sentiment.txt', 'r', encoding='latin-1') as f:
        for i, line in enumerate(f):
            line = line.strip().split('\t')
            label = int(line[0])
            labels.append(label)
            sentences.append(feature_extraction(line[1]))

    # tfidfを計算、文章をベクトル化
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(sentences).toarray()
    model = LogisticRegression().fit(features, labels)

    return vectorizer, model


def main():
    # 学習
    vectorizer1, model = create_model()

    text = input('レビュー:')
    sentences = [feature_extraction(text)]

    # インプットされたレビューの素性を学習モデルにあった形でベクトル化
    vectorizer = TfidfVectorizer(vocabulary=vectorizer1.vocabulary_)
    features = vectorizer.fit_transform(sentences).toarray()
    print(features)

    print(f'{model.predict(features)[0]} : {max(model.predict_proba(features)[0])}')


if __name__ == "__main__":
    main()
