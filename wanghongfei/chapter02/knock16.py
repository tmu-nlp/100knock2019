hightemp = open('/Users/hongfeiwang/documents/hightemp.txt').readlines()
num = int(input())
n_divide = []
for i in range(0,len(hightemp),num):
    n_divide.append("".join(hightemp[i:i+num]))

print("\n".join(n_divide))
# split -l n *.txt