with open("hightemp.txt", mode='r') as f:
    count = 0
    # 行の数をカウント
    for s_line in f:
        count += 1
    print(count)

# wc -l hightemp.txt
