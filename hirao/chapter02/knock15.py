n = int(input())
row_count = len(open('hightemp.txt').readlines())
with open('hightemp.txt', 'r') as f:
    index = 0
    for row in f:
        if index >= row_count - n:
            print(row.replace("\n", ""))
        index += 1

# tail -n 4 "hightemp.txt"
