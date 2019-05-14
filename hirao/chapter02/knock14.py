#冒頭n行のnを指定
n = int(input())
with open('hightemp.txt', 'r') as f:
    for i, row in enumerate(f):
        # 行数がnより少ない場合は表示する
        if i < n:
            print(row.replace("\n", ""))
        else:
            break

# head -n 4 "hightemp.txt"
