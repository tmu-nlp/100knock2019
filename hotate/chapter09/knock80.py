import bz2


def remove_noise(line):
    line_rem = list()
    for token in line.strip().split():
        token = token.strip(r'.,!?;:()[]\'\"')
        if len(token) > 0:
            line_rem.append(token)
    return ' '.join(line_rem)


def main():
    with open('knock80.100.txt', 'w') as f:
        for line in open('enwiki-20150112-400-r100-10576.txt', mode='r'):
            if line == '\n':
                continue
            cleaned_line = remove_noise(line)
            if len(cleaned_line) > 0:
                print(cleaned_line, file=f)


if __name__ == '__main__':
    main()
