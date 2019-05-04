def take_third(elem):
    return elem[2]
hightemp = open('/Users/hongfeiwang/documents/hightemp.txt').readlines()
row2list = []
for row in hightemp:
    row2list.append(row.split('\t'))
row2list.sort(key=take_third,reverse = True)
new_list = []
for row in row2list:
    new_list.append("\t".join(row))
print("".join(new_list))

