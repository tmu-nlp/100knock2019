'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
'''
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("N", type=int, help="ファイルの分割数N")
args = parser.parse_args()

# 1ファイルあたりの行数を計算
with open(args.input_file, "r") as f:
    num_line = math.ceil(sum(1 for line in f) / args.N)

with open(args.input_file, "r") as fr:
    for i in range(args.N):
        lines = [fr.readline() for line in range(num_line)]
        with open(f"result16-{i + 1}", "w") as fw:
            for line in lines:
                fw.write(line)

# split -l N hithtemp.txt