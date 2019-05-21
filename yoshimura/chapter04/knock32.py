'''
32. 動詞の原形
動詞の原形をすべて抽出せよ．
'''
from knock30 import get_morpheme_list

org_verbs = []
for sentence in get_morpheme_list("neko.txt.mecab"):
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            org_verbs.append(morpheme['base'])

print(org_verbs[:10])
