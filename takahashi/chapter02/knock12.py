# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

from knock10 import read_file

def extract_first_and_second_column(target: str) -> None:
    target = target.split("\n")

    # 各行をタブごとに分割し 1,2 列目だけ抽出する
    column1, column2 = "", ""
    for row in target:
        column1 += row.split("\t")[0] + "\n"
        column2 += row.split("\t")[1] + "\n"

    with open("./col1.txt", "w") as f1, open("./col2.txt", "w") as f2:
        f1.write(column1)
        f2.write(column2)

if __name__ == "__main__":
    target = read_file("hightemp.txt")
    extract_first_and_second_column(target)
