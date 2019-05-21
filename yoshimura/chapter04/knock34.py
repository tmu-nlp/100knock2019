'''
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
'''
from knock30 import get_morpheme_list

noun_phrases = []
for s in get_morpheme_list("neko.txt.mecab"):
    for i in range(len(s) - 2):
        if s[i]['pos'] == '名詞' and \
           s[i+1]['surface'] == 'の' and \
           s[i+2]['pos'] == '名詞':
            noun_phrases.append(
                s[i]['surface'] +
                s[i+1]['surface'] +
                s[i+2]['surface']
            )

print(noun_phrases[:10])
