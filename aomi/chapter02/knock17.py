set_list = set()

with open('hightemp.txt', 'r') as hightemp_file:
    for line in hightemp_file:
        line = line.split('\t')
        set_list.add(line[0])
print(len(set_list))
