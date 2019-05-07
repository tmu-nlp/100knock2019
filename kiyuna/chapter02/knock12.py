'''
12. 1 列目を col1.txt に，2 列目を col2.txt に保存
各行の 1 列目だけを抜き出したものを col1.txt に，
2 列目だけを抜き出したものを col2.txt としてファイルに保存せよ．
確認には cut コマンドを用いよ．
'''

fn = 'hightemp.txt'

with open('col1.txt', 'w') as f1, open('col2.txt', 'w') as f2:
    with open(fn, 'r') as f:
        for line in f:
            cols = line.rstrip().split('\t')
            f1.write(cols[0] + '\n')
            print(cols[1], file=f2)

# 別解
with open('col1.txt', 'w') as f:
    f.writelines(line.split()[0] + '\n' for line in open(fn))
