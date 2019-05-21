'''
31. 動詞
動詞の表層形をすべて抽出せよ．
'''
from knock30 import get_morpheme_list

verbs = []
for sentence in get_morpheme_list("neko.txt.mecab"):
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            verbs.append(morpheme['surface'])

print(verbs[:10])
