# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

from knock10 import read_file
import sys

def tail(target: str, line: int) -> str:
    target = target.split("\n")
    return "\n".join(target[len(target)-line:])

if __name__ == "__main__":
    args = sys.argv
    n = int(args[1])
    target = read_file("hightemp.txt")
    print(tail(target, n))