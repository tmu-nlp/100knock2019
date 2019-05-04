hightemp = open('/Users/hongfeiwang/documents/hightemp.txt').readlines()
print("tab version is",hightemp)
new_row = []
for row in hightemp:
    tab_split = row.split()
    space_join = ' '.join(tab_split) + '\n'
    new_row.append(space_join)
print("space version is",new_row)



