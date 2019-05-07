'''
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
'''
import sys

with open(sys.argv[1], "r") as f:
    for line in sorted(f, key=lambda x: x.split("\t")[2], reverse=True):
        print(line.rstrip())

# sort -k 3 -r hightemp.txt