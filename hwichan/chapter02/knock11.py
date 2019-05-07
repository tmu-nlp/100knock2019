import sys

with open('hightemp.txt', 'r') as file:
#     for line in file:
#         print(line.replace('\t',' ')) # \t : タブ

    # read() fileの内容をすべて読み込み文字列として返す
    s = file.read()
    s = s.replace('\t',' ')
    print(s)

# sedコマンド sed 's/置換前/置換後/g' filename
# 最後のgがない場合先頭のみ置換
