first = []
second = []
with open('col1.txt', 'r') as f:
    for row in f:
        first.append(row.replace("\n", ""))
with open('col2.txt', 'r') as f:
    for row in f:
        second.append(row.replace("\n", ""))
with open('hightemp_ver13.txt', 'w') as f:
    for i in range(len(first)):
        f.write(first[i] + "\t" + second[i] + "\n")

# !paste col1.txt col2.txt > "hightemp_ver13.txt"
