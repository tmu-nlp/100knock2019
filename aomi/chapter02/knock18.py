line_list = []
col3_list = []

with open('hightemp.txt', 'r') as hightemp_file:
    for i, line in enumerate(hightemp_file):
        line_list.append(line)
        line = line.split('\t')
        col3_list.append([float(line[2]), i])
sorted(col3_list)
for i in col3_list:
    print(line_list[i[1]], end = '')
