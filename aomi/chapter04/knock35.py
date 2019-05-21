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
    i = 0
    while i < len(line):
        tmp = []
        j = i
        while j < len(line):
            if line[j]['pos'] == '名詞':
                tmp.append(line[j]['surface'])
            else:
                j += 1
                break
            j += 1
        if len(tmp) >= 2:
            ans.append(''.join(tmp))
        i = j

print(ans)
