'''
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
'''
import sys
from collections import defaultdict
from operator import itemgetter

d = defaultdict(lambda: 0)

with open(sys.argv[1], "r") as f:
    for line in f:
        d[line.split("\t")[0]] += 1

for k, v in sorted(d.items(), key=itemgetter(1), reverse=True):
    print(f"{v}\t{k}")

# cut -f 1 hightemp.txt | sort | uniq -c | sort -r