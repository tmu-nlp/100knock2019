import itertools
from typing import Generator

from stemming.porter2 import stem

from knock51 import extract_word


def word_stem(filename: str = './nlp.txt') -> Generator[str, None, None]:
    """
    単語と stem のペアを返す
    """
    for word in extract_word(filename):
        s = stem(word)
        pair = f'{word}\t{s}'
        yield pair


def main(stop):
    for pair in itertools.islice(word_stem(), stop):
        print(pair)


if __name__ == '__main__':
    main(100)
