# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

from knock10 import read_file
from knock13 import write_file
import sys

def split(target: str, line: int) -> None:
    target = target.split("\n")
    for count in range(line):
        output = "\n".join(target[count*n : count*n+n])
        write_file(f"hightemp_{count}.txt", output)

if __name__ == "__main__":
    args = sys.argv
    n = int(args[1])
    target = read_file("hightemp.txt")
    split(target, n)

