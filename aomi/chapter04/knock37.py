import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.font_manager import FontProperties

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
ans = defaultdict(lambda: 0)
for line in result:
    for word in line:
        ans[word['surface']] += 1
x = []
y = []
for key, value in sorted(ans.items(), key=lambda x:-x[1]):
    x.append(key)
    y.append(value)
    if len(x) >= 10:
        break


plt.bar(x, y)
plt.show()
