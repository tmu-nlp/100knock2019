import re

with open('result_50.txt', 'r', encoding='utf-8') as i_file:
    with open('result_51.txt', 'w', encoding='utf-8') as o_file:
        for line in i_file.readlines():
            words = line.split()
            for word in words:
                word = word.strip('.,"\'-')
                if len(word) > 0:
                    print(word, file=o_file)
            print('', file=o_file)
