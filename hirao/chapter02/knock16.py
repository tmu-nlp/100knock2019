import math
n = int(input())
row_count = len(open('hightemp.txt').readlines())
n_list = []

max_num = math.ceil(row_count/n)
min_num = max_num - 1
min_row = max_num*n - row_count
for i in range(n - min_row):
    n_list.append(max_num)
for i in range(min_row):
    n_list.append(min_num)
ans_list = [[] for i in range(n)]
with open('hightemp.txt', 'r') as f:
    k = 0
    j = n_list[k]
    for i, row in enumerate(f):
        ans_list[k].append(row.replace("\n", ""))
        j -= 1
        if j == 0 and k < n-1:
            k += 1
            j = n_list[k]

for l in ans_list:
    for row in l:
        print(row)
    print("\n")

# split -l 7 "hightemp.txt" "./result16/"
