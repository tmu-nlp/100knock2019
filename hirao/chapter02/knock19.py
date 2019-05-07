import collections

l = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        l.append(row.replace("\n", "").split("\t")[0])
# counterにする
c = collections.Counter(l)
# 出現頻度順にソートする
for (s, count) in c.most_common():
    print(count, s)

# cut -f 1 "hightemp.txt" | sort | uniq -c | sort -r
