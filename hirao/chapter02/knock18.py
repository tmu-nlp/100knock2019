l = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        l.append(row.replace("\n", "").split("\t")[2])
for s in l[::-1]:
    print(s)

# cut -f 3 "hightemp.txt" | sort
