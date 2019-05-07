'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file1")
parser.add_argument("input_file2")
parser.add_argument("output_file")
args = parser.parse_args()

# 読み込み
with open(args.input_file1) as f1, open(args.input_file2) as f2:
    lines = [line1.rstrip() + "\t" + line2 for line1, line2 in zip(f1, f2)]

# 書き込み
with open(args.output_file, "w") as f:
    for line in lines:
        f.write(line)

# paste col1.txt col2.txt
