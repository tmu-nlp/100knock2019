'''
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
'''
from knock30 import get_morpheme_list

sa_nouns = []
for sentence in get_morpheme_list("neko.txt.mecab"):
    for morpheme in sentence:
        if morpheme['pos1'] == 'サ変接続':
            sa_nouns.append(morpheme['surface'])

print(sa_nouns[:10])