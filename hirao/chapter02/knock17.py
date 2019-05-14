l = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        # 1列目だけ取得
        l.append(row.split("\t")[0])
    # setで集合にする
    l = set(l)
print(l)


# cut -f 1 "hightemp.txt" | sort | uniq
