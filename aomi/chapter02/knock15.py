N = int(input())

line_list = []

with open('hightemp.txt', 'r') as hightemp_file:
    cnt = 0
    for line in hightemp_file:
        line_list.append(line)
line_list = line_list[::-1]
for i in range(N - 1, -1, -1):
    print(line_list[i], sep = '', end = '')
