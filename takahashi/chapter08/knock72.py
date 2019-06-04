# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
# 素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．

from sklearn.feature_extraction.text import TfidfVectorizer
from stemming.porter2 import stem
from knock71 import is_stopword
from typing import List, Tuple, Any
import pickle
import numpy as np


# ストップワード, 1文字の記号, "--" の除去とステミングの前処理
def preprocessor(sentence: str) -> str:
    res = []
    for word in sentence.split():
        if is_stopword(word) or len(word) < 1 or word == "--":
            continue
        res.append(stem(word))
    return " ".join(res)


# ファイルから素性を抽出する
def create_feature(filename: str) -> Tuple[List[str], List[int]]:
    sentences = []
    labels = []
    for line in open(filename, "r"):
        line = line.strip("\n")
        labels.append(int(line[:2]))
        sentences.append(preprocessor(line[3:]))
    return sentences, labels


def serialize(filename: str, data: Any) -> None:
    with open(f"./pickles/{filename}", "wb") as f:
        f.write(pickle.dumps(data, protocol=-1))


def deserialize(filename: str) -> Any:
    with open(f"./pickles/{filename}", "rb") as f:
        data = pickle.load(f)
    return data


def vectorize(sentences: List[str], labels: List[int]) -> None:
    # 文書を TF-IDF でベクトル化
    vectorizer = TfidfVectorizer()
    # 文ごとの語の出現頻度を元に tfidf を計算する
    features = vectorizer.fit_transform(sentences).toarray()

    # 使いそうなデータを pickle で保存しておく
    # 素性, ラベル, 語彙, 語彙の名前リスト
    serialize("features", features)
    serialize("labels", labels)
    serialize("vocabs", vectorizer.vocabulary_)
    serialize("names", vectorizer.get_feature_names())


if __name__ == "__main__":
    sentences, labels = create_feature("sentiment.txt")
    vectorize(sentences, labels)
