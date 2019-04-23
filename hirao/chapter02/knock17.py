l = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        l.append(row.split("\t")[0])
    l = set(l)
print(l)


# cut -f 1 "hightemp.txt" | sort | uniq
