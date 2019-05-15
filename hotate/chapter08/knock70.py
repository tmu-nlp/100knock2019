# -*- coding: utf-8 -*-
import os
import random
from typing import Tuple


def load_pos_neg_file(pos_file: str = 'rt-polarity.pos',
                      neg_file: str = 'rt-polarity.neg') -> Tuple[str, str]:
    for pos, neg in zip(open(pos_file, 'r', encoding='latin-1'), open(neg_file, 'r', encoding='latin-1')):
        yield pos, neg


def count_pos_neg(filename: str = 'sentiment.txt') -> Tuple[int, int]:
    pos_count = 0
    neg_count = 0
    for line in open(filename, 'r'):
        tag = line.split(' ')[0]
        if tag == '+1':
            pos_count += 1
        elif tag == '-1':
            neg_count += 1

    return pos_count, neg_count


def make_pos_neg_file(filename: str = 'sentiment.txt') -> None:
    sentence_tag_list = list()
    for pos, neg in load_pos_neg_file():
        sentence_tag_list.append(f'+1 {pos}')
        sentence_tag_list.append(f'-1 {neg}')

    random.shuffle(sentence_tag_list)

    with open(filename, 'w') as f:
        for line in sentence_tag_list:
            f.write(line)


def main():
    if not os.path.isfile('sentiment.txt'):
        make_pos_neg_file()

    print(count_pos_neg())


if __name__ == '__main__':
    main()
