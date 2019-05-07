n = int(input())
row_count = len(open('hightemp.txt').readlines())
with open('hightemp.txt', 'r') as f:
    for i, row in enumerate(f):
        # 末尾のn個だけ出力
        if i >= row_count - n:
            print(row.replace("\n", ""))

# tail -n 4 "hightemp.txt"
