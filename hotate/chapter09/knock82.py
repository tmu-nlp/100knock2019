import random
from collections import defaultdict


def word_context(filename='knock81.100.txt'):
    t_c_dict = defaultdict(list)
    for line in open(filename):
        words = line.strip().split()
        for i in range(len(words)):
            width = random.randint(1, 5)
            t = words[i]
            c_left = words[i - width: i]
            c_right = words[i + 1: i + width + 1]
            c = ' '.join(c_left + c_right)
            t_c_dict[t].append(c)

    return t_c_dict


def main():
    t_c_dict = word_context()

    with open('knock82.100.txt', 'w') as f:
        for t, c_list in t_c_dict.items():
            for c in c_list:
                print(f'{t}\t{c}', file=f)


if __name__ == '__main__':
    main()
