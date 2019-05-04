hightemp = open('/Users/hongfeiwang/documents/hightemp.txt').readlines()
num = int(input())
n_row = []
for i in range(num):
    n_row.append(hightemp[i])
print(''.join(n_row))
# head -n hightemp.txt