from knock05 import n_gram

str1 = "paraparaparadise"
str2 = "paragraph"
n = 2

X = set(n_gram(str1, n))
Y = set(n_gram(str2, n))

print(f"{X | Y}")
print(f"{X & Y}")
print(f"{X - Y}")

if "se" in X:
    print("Xに含まれる")
else:
    print("Xに含まれない")

if "se" in Y:
    print("Yに含まれる")
else:
    print("Yに含まれない")