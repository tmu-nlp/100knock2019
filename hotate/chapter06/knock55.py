from knock53 import load_token


def main():
    for token in load_token():
        if token.is_person():
            print(token.word)


if __name__ == '__main__':
    main()
