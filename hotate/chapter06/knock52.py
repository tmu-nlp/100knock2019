from stemming.porter2 import stem
from knock51 import extract_word


def word_stem(filename='./nlp.txt'):
    """
    単語と stem のペアを返す
    """
    for word in extract_word(filename):
        s = stem(word)
        pair = f'{word}\t{s}'
        yield pair


if __name__ == '__main__':
    import itertools
    for pair in itertools.islice(word_stem(), 100):
        print(pair)
