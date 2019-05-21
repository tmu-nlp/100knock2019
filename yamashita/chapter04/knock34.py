from knock30 import load_morpheme

path = 'neko.txt.mecab'
result = load_morpheme(path)

ans = []
for sentence in result:
    for i in range(len(sentence)-2):
        if sentence[i]['pos'] == '名詞' and sentence[i+1]['pos1'] == '連体化' and sentence[i+2]['pos'] == '名詞':
            ans.append(sentence[i]['surface']+sentence[i+1]['surface']+sentence[i+2]['surface'])

print(ans)