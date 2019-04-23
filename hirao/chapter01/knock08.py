def cipher(s):
    output = ""
    for i in range(len(s)):
        c = s[i]
        c_out = ord(c)
        if ord('a') <= ord(c) <= ord('z'):
            c_out = 219 - c_out
        output += chr(c_out)
    return output


s = "My name is Reo Hirao"
print(s)
s = cipher(s)
print(s)
s = cipher(s)
print(s)
