from knock30 import load_morpheme
from collections import defaultdict


def calc_word_frequency(result):
    words = defaultdict(lambda: 0)
    for sentence in result:
        for morpheme in sentence:
            words[morpheme['surface']] += 1
    return words


if __name__ == '__main__':
    path = 'neko.txt.mecab'
    result = load_morpheme(path)
    words = calc_word_frequency(result)
    # print(sorted(words.items(), key = lambda x: x[1], reverse = True))
    for key, value in sorted(words.items(), key=lambda x: x[1], reverse=True):
        print(f'{key}\t{value}')
