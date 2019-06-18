def is_stopword(word: str) -> bool:
    stopwords = ['the', 'of', 'and', 'a', 'to', 'in',
                 'that', 'his', 'it', 'I', 's', 'is', 'he',
                 'with', 'was', 'as', 'all', 'for', 'this',
                 '!', 'at', 'by', 'but', 'not', 'him', 'from',
                 'be', 'on', 'so']

    return (word in stopwords)
