from knock30 import load_morpheme

path = 'neko.txt.mecab'
result = load_morpheme(path)

ans = []
for sentence in result:
    for morpheme in sentence:
        if morpheme['pos'] == '名詞' and morpheme['pos1'] == 'サ変接続':
            # print(morpheme)
            ans.append(morpheme)

print(ans)