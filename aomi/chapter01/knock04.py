s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.split(' ')
list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}
for i in range(len(s)) :
    if i + 1 in list :
        ans[s[i][0]] = i + 1
    else :
        t = s[i][0] + s[i][1]
        ans[t] = i + 1
print(ans)
