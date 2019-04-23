# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

from knock10 import read_file

def uniq_first_column(target: str) -> str:
    target = target.split("\n")
    column = []
    for col1 in target:
        column.append(col1.split("\t")[0])

    return set(column)

if __name__ == "__main__":
    target = read_file("hightemp.txt")
    print(uniq_first_column(target))
