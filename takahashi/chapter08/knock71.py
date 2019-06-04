# 71. ストップワード
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
# さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
# さらに，その関数に対するテストを記述せよ．

from nltk.corpus import stopwords


# ストップワードのリストに含まれているかの判定
def is_stopword(word: str) -> bool:
    return word in set(stopwords.words("english"))


# is_stopword 関数のテスト
def test_is_stopword() -> None:
    test_words = [
        ("of", True),
        ("get", False),
        ("am", True),
        ("not", True),
        ("stopword", False),
    ]
    for word, expect in test_words:
        assert is_stopword(word) == expect, f"expect: {expect} [{word}]"


if __name__ == "__main__":
    test_is_stopword()

"""
stopwords
 - https://gist.github.com/sebleier/554280
 - https://gist.github.com/sebleier/554280#gistcomment-2637371
"""
