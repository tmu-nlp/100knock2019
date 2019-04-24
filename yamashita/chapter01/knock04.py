s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
li = s.split()
dic = {}
for i in range(len(li)):
    if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dic[li[i][0]] = i+1
    else:
        dic[li[i][:2]] = i+1

print(dic)
