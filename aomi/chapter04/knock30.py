import MeCab

'''
with open('neko.txt', 'r') as neko_file, open('neko.txt.mecab', 'w') as mecab_file:
     mecab = MeCab.Tagger()
     mecab_file.write(mecab.parse(neko_file.read()))
'''

with open('neko.txt.mecab', 'r') as mecab_file:
    res = []
    for line in mecab_file:
        col1 = line.split('\t')
        col2 = col1[1].split(',')
        tmp = {'surface': col1[0], 'base': col2[6], 'pos': col2[0], 'pos1': col2[1]}
        res.append(tmp)

        if col1[0] == '。':
            res = []
