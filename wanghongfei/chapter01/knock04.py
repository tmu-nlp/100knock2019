str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
       "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str2 = str1.replace(".", '')
w_list = str2.split(' ')
dict2 = {}
counter = 0
head = (0, 4, 5, 6, 7, 8, 14, 15, 18)
for word in w_list:
    if counter in head:
        dict2[counter] = word[0]

    else:
        dict2[counter] = word[0:2]
    counter += 1
print(dict2)
