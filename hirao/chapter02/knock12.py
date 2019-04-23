first = []
second = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        first.append(row.split("\t")[0])
        second.append(row.split("\t")[1])
with open('col1.txt', 'w') as f:
    for s in first:
        f.write(s + "\n")
with open('col2.txt', 'w') as f:
    for s in second:
        f.write(s + "\n")

# cut -f 1 "hightemp.txt" > "col1.txt"
# cut -f 2 "hightemp.txt" > "col2.txt"
