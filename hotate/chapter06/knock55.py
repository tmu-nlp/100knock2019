from knock53 import load_token


if __name__ == '__main__':
    for token in load_token():
        if token.is_person():
            print(token.word)
