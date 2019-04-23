s = "paraparaparadise"
t = "paragraph"

X = []
for i in range(len(s) - 1):
    X.append(s[i] + s[i + 1])
X = set(X)

Y = []
for i in range(len(t) - 1):
    Y.append(t[i] + t[i + 1])
Y = set(Y)

A = X | Y
B = X & Y
C = X - Y

if "se" in X:
    print("X: YES")
else:
    print("X: NO")

if "se" in Y:
    print("Y: YES")
else:
    print("Y: NO")

print(A)
print(B)
print(C)
