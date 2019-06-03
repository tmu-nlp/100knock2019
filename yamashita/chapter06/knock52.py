import snowballstemmer

with open('result_51.txt', 'r', encoding='utf-8') as i_file:
    stemmer = snowballstemmer.stemmer('english')
    for line in i_file.readlines():
        print(f'{line.strip()}\t{stemmer.stemWord(line.strip())}')
