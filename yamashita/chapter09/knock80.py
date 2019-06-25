from tqdm import tqdm


def main():
    with open('result_knock80.txt', 'w', encoding='utf-8') as w_file:
        with open('enwiki-20150112-400-r100-10576.txt', 'r', encoding='utf-8') as i_file:
            for line in tqdm(i_file):
                tokens = []
                words = line.strip().split()
                for word in words:
                    token = word.strip('.,!?;:()[]\'\"')
                    if token == '':
                        continue
                    tokens.append(token)
                if not tokens:
                    continue
                print(' '.join(tokens), file=w_file)


if __name__ == '__main__':
    main()
