'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file1")
parser.add_argument("output_file2")
args = parser.parse_args()

# 読み込み
col1, col2 = [], []
with open(args.input_file, "r") as f:
    for line in f:
        col1.append(line.split("\t")[0])
        col2.append(line.split("\t")[1])

# 書き込み
with open(args.output_file1, "w") as f1, open(args.output_file2, "w") as f2:
    for line1, line2 in zip(col1, col2):
        f1.write(line1 + "\n")
        f2.write(line2 + "\n")

# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt