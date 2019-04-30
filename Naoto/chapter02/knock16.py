import sys

n = int(sys.argv[1])

lines = []

for line in sys.stdin:
    lines.append(line)

line_num = len(lines)
split_num = line_num / n

count = 0
n = 1

for line in lines:
    if count % split_num == 0:
        opt = open("hightemp_" + str(n) + ".txt", "w")
        n += 1
    count += 1
    line = line.strip()
    opt.write(line)
    if count % split_num == 0:
        opt.close()
    else:
        opt.write("\n")