# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

from knock10 import read_file

def replace_tabs_with_spaces(target: str) -> str:
    return target.replace("\t", " ")

if __name__ == "__main__":
    target = read_file("hightemp.txt")
    print(replace_tabs_with_spaces(target))