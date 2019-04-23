s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
drop = ",."
print(s)

for c in list(drop):
    s = s.replace(c, "")
s = s.split()

display_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans_dict = {}
for i, word in enumerate(s):
    if i + 1 in display_list:
        ans = word[0]
    else:
        ans = word[:2]
    ans_dict[ans] = i + 1

print(ans_dict)
