# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        file = f.read()
    return file

def count_lines(target: str) -> int:
    # 文字列の改行数で行数を求める
    return (len(target.split("\n")))

if __name__ == "__main__":
    target = read_file("hightemp.txt")
    print(count_lines(target))