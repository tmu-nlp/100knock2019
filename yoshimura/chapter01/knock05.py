
def word_ngram(s: str, n: int) -> list:
    word_list = s.split()
    return [word_list[i:i + n] for i in range(len(word_list) - n + 1)]


def char_ngram(s: str, n: int) -> list:
    return [s[i:i + n] for i in range(len(s) - n + 1)]


if __name__ == "__main__":
    s = "I am an NLPer"
    n = 3

    print(f"単語{n}gram : {word_ngram(s, n)}")
    print(f"文字{n}gram : {char_ngram(s, n)}")

# 関数, typehint, __name__ 