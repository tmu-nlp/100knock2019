from tqdm import tqdm


def main():
    replace_list = []
    with open('countries.txt', 'r', encoding='utf-8') as c_file:
        for line in c_file:
            words = line.strip().split()
            replace_list.append((' '.join(words), '_'.join(words)))

    with open('result_knock81.txt', 'w', encoding='utf-8') as w_file:
        with open('result_knock80.txt', 'r', encoding='utf-8') as i_file:
            for line in tqdm(i_file):
                for before, after in replace_list:
                    line = line.strip().replace(before, after)
                print(f'{line}', file=w_file)


if __name__ == '__main__':
    main()
