str1 = 'パトカー'
str2 = 'タクシー'
str3 = ''
index1 = 0
index2 = 0
loop = 0

while loop < 8:
    if loop % 2 == 0:
        str3 = str3 + str1[index1]
        index1 += 1
    else:
        str3 = str3 + str2[index2]
        index2 += 1
    loop += 1
print(str3)

