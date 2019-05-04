col1 = open('./col1.txt').readlines()
del_space = []
for str in col1:
    del_space.append(str.strip())
col2 = open('./col2.txt').readlines()
merge_col = []
for i in range(len(col1)):
    merge_col.append(del_space[i] + "\t" + col2[i])
print(''.join(merge_col))

