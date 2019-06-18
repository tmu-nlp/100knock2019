import random


def main():
    result = []
    with open('rt-polarity.pos', 'r', encoding='latin-1') as pos_file:
        for line in pos_file:
            result.append(f'1 {line.rstrip()}')

    with open('rt-polarity.neg', 'r', encoding='latin-1') as neg_file:
        for line in neg_file:
            result.append(f'-1 {line.rstrip()}')

    random.shuffle(result)
    with open('sentiment.txt', 'w', encoding='utf-8') as w_file:
        for line in result:
            print(line, file=w_file)


if __name__ == '__main__':
    main()
