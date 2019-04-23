from itertools import zip_longest

str1 = "パトカー"
str2 = "タクシー"

result = ""
for s1, s2 in zip_longest(str1, str2, fillvalue=""):
    result += s1 + s2

print(result)

# zip, zip_longest
