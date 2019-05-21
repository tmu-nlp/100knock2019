import MeCab
import re

def load_morpheme(path):
    morpheme = {}
    sentence = []
    result = []
    with open(path,'r',encoding='utf-8') as input_file:
        for line in input_file:
            line = line.rstrip()
            if line != 'EOS':
                splited = re.split('[\t,]',line)
                morpheme = {'surface':splited[0],'base':splited[7],'pos':splited[1],'pos1':splited[2]}
                sentence.append(morpheme)
                if splited[2] == '句点':
                    result.append(sentence[:])
                    sentence.clear()
    return result


if __name__ == '__main__':
    path = 'neko.txt.mecab'
    result = load_morpheme(path)
    for line in result:
        print(line)
    