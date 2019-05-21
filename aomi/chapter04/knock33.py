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
    for word in line:
        if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
            ans.append(word['surface']);

for i in range(30):
    print(ans[i])
