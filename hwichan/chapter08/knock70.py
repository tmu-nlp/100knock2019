import random


def main():
    text_list = []

    with open('rt-polaritydata/rt-polarity.neg', 'r', encoding='latin-1') as f:
        for line in f:
            text_list.append('-1\t{}'.format(line))

    with open('rt-polaritydata/rt-polarity.pos', 'r', encoding='latin-1') as f:
        for line in f:
            text_list.append('+1\t{}'.format(line))

    random.shuffle(text_list)

    with open('sentiment.txt', 'w', encoding='latin-1') as f:
        f.write(''.join(text_list))

    pos = 0
    neg = 0
    with open('sentiment.txt', 'r', encoding='latin-1') as f:
        for line in f:
            line = line.split('\t')[0]
            if line == '+1':
                pos += 1
            else:
                neg += 1

    print(f'pos {pos}, neg {neg}')


if __name__ == '__main__':
    main()
