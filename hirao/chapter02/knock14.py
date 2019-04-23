n = int(input())
with open('hightemp.txt', 'r') as f:
    index = 0
    for row in f:
        if index < n:
            print(row.replace("\n", ""))
        index += 1

# head -n 4 "hightemp.txt"
