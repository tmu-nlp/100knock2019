N = int(input())

line_list = []

with open('hightemp.txt', 'r') as hightemp_file:
    for line in hightemp_file:
        line_list.append(line)

cnt = len(line_list)
split_list = [cnt // N] * N
for i in range(cnt % N):
    split_list[i] += 1

p = 0
for i, n in enumerate(split_list):
    with open('splitfile{0}'.format(i), 'w') as split_file:
        for line in line_list[p:p + n:1]:
            print(line, end = '', file = split_file)
    p += n
