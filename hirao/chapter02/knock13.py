#1列目、2列目の要素を格納するリスト
first = []
second = []
#col1.txtとcol2.txtから要素を読み込む
with open('col1.txt', 'r') as f:
    for row in f:
        first.append(row.replace("\n", ""))
with open('col2.txt', 'r') as f:
    for row in f:
        second.append(row.replace("\n", ""))
#新しいファイルに1列目と2列目を出力
with open('hightemp_ver13.txt', 'w') as f:
    for i in range(len(first)):
        f.write(first[i] + "\t" + second[i] + "\n")

# !paste col1.txt col2.txt > "hightemp_ver13.txt"
