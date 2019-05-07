'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("N", type=int, help="末尾のN行")
args = parser.parse_args()

line_num = sum(1 for _ in open(args.input_file, "r"))
for i, line in enumerate(open(args.input_file, "r"), 1):
    if i > line_num - args.N:
        print(line.rstrip())

# tail -n N hightemp.txt