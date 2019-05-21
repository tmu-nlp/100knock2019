from knock30 import load_morpheme

path = 'neko.txt.mecab'
result = load_morpheme(path)

noun_list = []
ans = []
for sentence in result:
    for morpheme in sentence:
        if morpheme['pos'] == '名詞':
            noun_list.append(morpheme['surface'])
        else:
            if len(noun_list) > 1:
                ans.append(''.join(noun_list))
            noun_list.clear()
        
print(ans)