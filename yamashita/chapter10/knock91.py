def main():
    data_path = 'questions-words.txt'
    output_path = 'result_91.txt'

    with open(data_path, 'r', encoding='utf-8') as d_file, open(output_path, 'w', encoding='utf-8') as o_file:
        flag = False
        for line in d_file:
            if line.strip() == ': family':
                flag = True
                continue
            if not flag:
                continue
            if line.strip()[0] == ':':
                break

            print(line.rstrip(), file=o_file)


if __name__ == '__main__':
    main()
