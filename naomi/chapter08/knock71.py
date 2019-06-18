stopwords = ['the', 'of', 'and', 'a', 'to', 'in',
             'that', 'his', 'it', 'I', 's', 'is', 'he',
             'with', 'was', 'as', 'all', 'for', 'this',
             '!', 'at', 'by', 'but', 'not', 'him', 'from',
             'be', 'on', 'so']

def is_stopword(word: str, stopwrods: list) -> bool:
    return (word in stopwords)