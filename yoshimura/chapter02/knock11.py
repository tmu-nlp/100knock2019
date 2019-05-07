'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''
import sys

# 読み込み
with open(sys.argv[1], "r") as f:
    for line in f:
        print(line.rstrip().replace("\t", " "))

# sed -e 's/    //g' hightemp.txt
# https://rcmdnk.com/blog/2016/09/13/computer-gnu-bsd-linux-mac/

# tr '\t' ' ' < hightemp.txt

# expand -t 1 hightemp.txt
# https://webkaru.net/linux/expand-command/