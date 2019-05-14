'''
19. 各行の 1 コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の 1 列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認には cut, uniq, sort コマンドを用いよ．
'''
from collections import defaultdict

cnt = defaultdict(int)

with open('hightemp.txt', 'r') as f:
    for line in f:
        cols = line.rstrip().split('\t')
        cnt[cols[0]] += 1

with open('out19', 'w') as f:
    for k, v in sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True):
        print(f'{v:4d} {k}', file=f)
