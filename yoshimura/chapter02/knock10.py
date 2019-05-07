'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''
import sys

with open(sys.argv[1], "r") as f:
    print(sum(1 for _ in f))

# wc -l hightemp.txt
