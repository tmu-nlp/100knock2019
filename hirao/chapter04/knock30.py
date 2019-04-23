import re
SIZE = 10

def load_txt(file_name: str) -> list:
    # [{ surface: , base: , pos:, pos1:, }]
    word_list = []
    for line in open(file_name, encoding='utf8'):
        if line == 'EOS\n':
            continue
        splited = re.split('[\t,]', line.strip())
        word_params= {
            'surface': splited[0],
            'base'   : splited[7],
            'pos'    : splited[1],
            'pos1'   : splited[2],
        }
        word_list.append(word_params)
    return word_list

if __name__ == '__main__':
    word_list = load_txt("neko.txt.mecab")
    for i in range(SIZE):
        print(word_list[i])
