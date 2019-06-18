from nltk.corpus import stopwords


def is_stopword(s):
    stopwords_list = set(stopwords.words('english'))
    return s.lower() in stopwords_list


def test_stopword():
    print(f'nlp : {is_stopword("nlp")}')
    print(f'and : {is_stopword("and")}')
    print(f'By : {is_stopword("By")}')
    print(f'Gorilla : {is_stopword("Gorilla")}')


if __name__ == '__main__':
    test_stopword()
