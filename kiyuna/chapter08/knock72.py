'''
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
'''
import sys
import pickle
from nltk.stem.porter import PorterStemmer as PS
from sklearn.feature_extraction.text import TfidfVectorizer
from knock71 import is_stopword


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


def check(stem):
    if is_stopword(stem):
        return False
    if len(stem) == 1:
        return False
    return True


def extract_features(file_path):
    ps = PS()
    labels, docs = [], []
    for line in open(file_path):
        label, *sentence = line.split()
        tokens = [stem for stem in map(ps.stem, sentence) if check(stem)]
        labels.append(int(label))
        docs.append(" ".join(tokens))
    return labels, docs


def save(file_name, data):
    with open(f"./pickles/{file_name}", 'wb') as f_out:
        pickle.dump(data, f_out)


def load(file_name):
    with open(f"./pickles/{file_name}", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


def vectorize_and_save(labels, docs):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(docs).toarray()

    save("features", features)
    save("labels", labels)
    save("vocabs", vectorizer.vocabulary_)
    save("names", vectorizer.get_feature_names())
    message(sorted(vectorizer.vocabulary_.items(), key=lambda x: -x[1])[:30])


if __name__ == "__main__":
    labels, docs = extract_features("./sentiment.txt")
    vectorize_and_save(labels, docs)


'''
* 問題文の意味がわからない人のための 言語処理100本ノック 第8章 機械学習
https://qiita.com/Masaaki_Inaba/items/ddb687daf9e67461a3f7


* TF-IDF, TfidfVectorizer
http://ailaby.com/tfidf/
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

- get_feature_names(self)
    [Methods] Array mapping from feature integer indices to feature name


* pickle モジュール
https://docs.python.org/ja/3/library/pickle.html
'''
