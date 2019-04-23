import re
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list1 = re.split('[., ]',str)
list2 = [x for x in list1 if x is not ""]

num_list = [1,5,6,7,8,9,15,16,19]

list3 = {}
for i in range(len(list2)):
    x = list2[i]
    if i+1 in num_list:
        list3[x[:1]] = list2[i]
    else:
        list3[x[:2]] = list2[i]

# print(list1)
# print(list2)
print(list3)
