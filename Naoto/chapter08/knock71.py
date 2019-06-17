'''
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
'''
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords


stopwords_ = ["world", "wide", "web"]


def is_stopword_mine(str_):
    for word in stopwords_:
        if word in str_:
            return True
    return False


def is_stopword(word: str) -> bool:
    return word in set(stopwords.words())


def test_is_stopword():
    test_case = [
        ["world", True],
        ["wide", True],
        ["web", True],
        ["fire", False],
        ["water", False], 
        ["Utada", False],
        ["Hikaru", False],
        ["is", False],
        ["genius", False]
    ]
    for test in test_case:
        if is_stopword_mine(test[0]) == test[1]:
            print("OK")
        else:
            print("NG")


if __name__ == "__main__":
    # test_is_stopword()
    print(is_stopword_takahashi("of"))
