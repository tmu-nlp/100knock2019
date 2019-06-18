'''
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
'''


from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from typing import List, Tuple, Any
from tqdm import tqdm


def serialize(filename: str, data: Any) -> None:
    with open(f"./pickles/{filename}", "wb") as f:
        f.write(pickle.dumps(data, protocol=-1))


def deserialize(filename: str) -> Any:
    with open(f"./pickles/{filename}", "rb") as f:
        data = pickle.load(f)
    return data


def labels_sentences(feature="features.txt"):
    labels = []
    sentences = []
    with open(feature, "r", encoding="latin-1") as f:
        pbar = tqdm(total=10662)
        for line in f:
            line = line.rstrip()
            labels.append(int(line[:2]))
            sentences.append(line[3:])
            pbar.update(1)
    pbar.close()
    return labels, sentences


def logistic(feature="features.txt"):
    labels, sentences = labels_sentences(feature)
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(sentences).toarray()
    model = LogisticRegression(solver='lbfgs').fit(features, labels)
    serialize("model", model)
    serialize("labels", labels)
    serialize("features", features)
    serialize("vocabs", vectorizer.vocabulary_)
    serialize("names", vectorizer.get_feature_names())


if __name__ == "__main__":
    logistic()
