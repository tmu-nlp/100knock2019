'''
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ
'''
from knock30 import get_morpheme_list

compound_nouns = []
longest_match = []
for sentence in get_morpheme_list("neko.txt.mecab"):
    for morpheme in sentence:
        if morpheme['pos'] == '名詞':
            longest_match.append(morpheme['surface'])
        elif len(longest_match) > 1:
            compound_nouns.append(''.join(longest_match))
            longest_match.clear()
        else:
            longest_match.clear()

print(compound_nouns[:15])
