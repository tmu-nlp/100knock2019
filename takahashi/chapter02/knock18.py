# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

from knock10 import read_file

def sort_by_third_column(target: str) -> str:
    target = target.split("\n")
    # 行で分割されている各要素を tab で分割する
    target = [t.split("\t") for t in target]
    
    # 各行を 3 番目の要素を key としてソートする
    target = sorted(target, key=lambda x:x[2], reverse=True)

    return "\n".join(["\t".join(elem) for elem in target])

if __name__ == "__main__":
    target = read_file("hightemp.txt")
    print(sort_by_third_column(target))
