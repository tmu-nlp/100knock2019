l = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = l.split()
ans = []
list = [0,4,5,6,7,8,14,15,18]
words_dict= {}
count = 0

for  i in range(len(words)):
    if i in list:
        ans.append(words[i][0])
    else:
        ans.append(words[i][0:2])

for i in range(len(words)):
    words_dict[ans[i]] = i

print(words_dict)

        


