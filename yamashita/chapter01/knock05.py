def n_gram(target, n):
    ngram = []
    for i in range(len(target)):
        if len(target[i:i+n]) == n:
            ngram.append(target[i:i+n])

    return ngram


if __name__ == "__main__":
    s = "I am an NLPer"
    char_ngram = s.replace(" ", "")
    word_ngram = s.split()
    n = 2

    print(n_gram(char_ngram, n))
    print(n_gram(word_ngram, n))
