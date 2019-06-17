from knock71 import is_stopword
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import snowballstemmer
stemmer = snowballstemmer.stemmer('english')  # stemmingモジュール読み込み


def feature_extraction(text: str):
    words = text.split(' ')
    sentence = []
    for word in words:
        if is_stopword(word) or len(word) == 1:
            continue
        sentence.append(stemmer.stemWord(word))

    return ' '.join(sentence)


def main():
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

    # 引数にベクトル化した文章と正解ラベルを指定することでmodelを学習
    model = LogisticRegression().fit(features, labels)


if __name__ == "__main__":
    main()
