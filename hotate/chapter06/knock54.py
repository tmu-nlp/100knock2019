if __name__ == '__main__':
    import itertools
    from knock53 import load_token

    for token in itertools.islice(load_token(), 50):
        print(f'{token.word}\t{token.lemma}\t{token.pos}')
