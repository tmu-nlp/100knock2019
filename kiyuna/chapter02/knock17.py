'''
17. １列目の文字列の異なり
1 列目の文字列の種類（異なる文字列の集合）を求めよ．確認には sort, uniq コマンドを用いよ．
'''
s = set()
with open('hightemp.txt', 'r') as f:
    for line in f:
        cols = line.rstrip().split('\t')
        s.add(cols[0])

with open('out17', 'w') as f:
    for e in sorted(s):
        print(e, file=f)
