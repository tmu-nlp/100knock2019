'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("N", type=int, help="先頭のN行")
args = parser.parse_args()

with open(args.input_file, "r") as f:
    for i in range(args.N):
        print(f.readline().rstrip())

# head -n 5 hightemp.txt
