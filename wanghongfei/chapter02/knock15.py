hightemp = open('/Users/hongfeiwang/documents/hightemp.txt').readlines()
num = int(input())
n_row = []
for i in range(len(hightemp) - num,len(hightemp)):
    n_row.append(hightemp[i])
print(''.join(n_row))