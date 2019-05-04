hightemp = open('/Users/hongfeiwang/documents/hightemp.txt').readlines()
col1 = []
col2 = []
for row in hightemp:
    split = row.split()
    col1.append(split[0])
    col2.append(split[1])
province = '\n'.join(col1)
city = '\n'.join(col2)
print("col1 is:\n",province)
print("col2 is:\n",city)
file1 = open('col1.txt','w')
file1.write(province)
file1.close()
file2 = open('col2.txt','w')
file2.write(city)
file2.close()
# cut -f1 hightemp.txt
# cut -f2 hightemp.txt

