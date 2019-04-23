from knock05 import char_ngram

X = set(char_ngram("paraparaparadise", 2))
Y = set(char_ngram("paragraph", 2))

print(f"XとYの和集合 : {X | Y}")
print(f"XとYの積集合 : {X & Y}")
print(f"XとYの差集合 : {X - Y}")

print(f"seがXに含まれる : {'se' in X}")
print(f"seがYに含まれる : {'se' in Y}")

# 自作モジュールのimport, set, setの演算