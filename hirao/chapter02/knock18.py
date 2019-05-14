l = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        l.append(row.replace("\n", "").split("\t"))
# x[2]でソート
l.sort(key=lambda x: x[2])
for s in l:
    print("{}\t{}\t{}\t{}".format(s[0], s[1], s[2], s[3]))

# cut -f 3 "hightemp.txt" | sort
