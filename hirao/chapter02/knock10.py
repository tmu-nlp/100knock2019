with open("hightemp.txt", mode='r') as f:
    count = 0
    for s_line in f:
        count += 1
    print(count)

# wc -l hightemp.txt
