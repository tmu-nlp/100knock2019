'''
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
'''
import sys

with open(sys.argv[1], "r") as f:
    for unique in {line.split("\t")[0] for line in f}:
        print(unique)

# cut -f 1 hightemp.txt | sort | uniq
