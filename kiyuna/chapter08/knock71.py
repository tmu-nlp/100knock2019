'''
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
'''
import sys
from nltk.corpus import stopwords


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


stop_words = set(stopwords.words('english'))


def is_stopword(word):
    """
    >>> is_stopword("the")
    True
    >>> is_stopword("NLP")
    False
    """
    return word in stop_words


if __name__ == '__main__':
    message(sorted(stop_words))

    # tokens = open('sentiment.txt').read().split()
    # d = {word: tokens.count(word) for word in stop_words}
    # for k, v in sorted(d.items(), key=lambda x: -x[1]):
    #     print(k, v)

    import doctest
    doctest.testmod()   # -v を付けるとログが出力される


'''
* stopword
https://en.wikipedia.org/wiki/Stop_words
-> the most common words in a language


* NLTK の Stopwords Corpus
$ python -c "import nltk; nltk.download('stopwords')"

This corpus contains lists of stop words for several languages.  These
are high-frequency grammatical words which are usually ignored in text
retrieval applications.

- They were obtained from:
http://anoncvs.postgresql.org/cvsweb.cgi/pgsql/src/backend/snowball/stopwords/

- The English list has been augmented
https://github.com/nltk/nltk_data/issues/22


* doctest モジュール
https://docs.python.org/ja/3/library/doctest.html
'''
