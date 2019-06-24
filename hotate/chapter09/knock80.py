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
        for line in bz2.open('enwiki-20150112-400-r100-10576.txt.bz2', mode='rb'):
            print(remove_noise(line.decode('utf-8')), file=f)


if __name__ == '__main__':
    main()
