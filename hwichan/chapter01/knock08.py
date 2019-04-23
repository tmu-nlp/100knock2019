def ciper(str):
    r_str = ''
    for i in str:
        if i.islower(): #小文字ならTrue
            r_str += chr(219-ord(i)) #chr:アスキーから文字に変換 ord:文字からアスキー
        else:
            r_str += i

    return r_str

str = "My name is HwiChan"
c_str = ciper(str)

print(str)
print(c_str)
print(ciper(c_str))
