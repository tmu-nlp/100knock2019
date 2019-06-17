from knock73 import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def create_model(filename: str):
    sentences = []
    labels = []
    with open(filename, 'r', encoding='latin-1') as f:
        for i, line in enumerate(f):
            line = line.strip().split('\t')
            label = int(line[0])
            labels.append(label)
            sentences.append(feature_extraction(line[1]))

    # tfidfを計算、文章をベクトル化
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(sentences).toarray()
    model = LogisticRegression().fit(features, labels)

    return labels, features, model


def main():
    # 学習
    labels, features, model = create_model('sentiment.txt')

    predicts = model.predict(features)  # 予測ラベル
    predict_probas = model.predict_proba(features) # 予測確率

    result = []
    for label, predict, predict_proba in zip(labels, predicts, predict_probas):
        result.append(f'{label}\t{predict}\t{max(predict_proba)}')


    with open('result.txt', 'w') as f:
        f.write('\n'.join(result))


if __name__ == "__main__":
    main()
