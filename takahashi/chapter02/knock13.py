# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ
# 確認にはpasteコマンドを用いよ．

from knock10 import read_file

def write_file(filename: str, target: str) -> None:
    with open(filename, "w") as f:
        f.write(target)

def merge_two_column(target1: str, target2: str) -> None:
    col1 = target1.split("\n")
    col2 = target2.split("\n")

    output = ""
    for c1, c2 in zip(col1, col2):
        output += c1 + "\t" + c2 + "\n"

    write_file("output.txt", output)

if __name__ == "__main__":
    target1 = read_file("col1.txt")
    target2 = read_file("col2.txt")

    merge_two_column(target1, target2)