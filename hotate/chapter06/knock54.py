import itertools
from knock53 import load_token


def main(stop):
    for token in itertools.islice(load_token(), stop):
        print(f'{token.word}\t{token.lemma}\t{token.pos}')


if __name__ == '__main__':
    main(50)
