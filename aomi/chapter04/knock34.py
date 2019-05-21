def getdata():
    with open('neko.txt.mecab', 'r') as mecab_file:
        res = []
        for line in mecab_file:
            col1 = line.split('\t')
            if len(col1) == 1:
                continue
            col2 = col1[1].split(',')
            tmp = {'surface': col1[0], 'base': col2[6], 'pos': col2[0], 'pos1': col2[1]}
            res.append(tmp)
            if col1[0] == '。':
                yield res
                res = []

result = getdata()
ans = []
for line in result:
    for i in range(1, len(line) - 1):
        if line[i]['surface'] == 'の' and line[i - 1]['pos'] == '名詞' and line[i + 1]['pos'] == '名詞':
            ans.append(line[i - 1]['surface'] + line[i]['surface'] + line[i + 1]['surface'])

for i in range(30):
    print(ans[i])
