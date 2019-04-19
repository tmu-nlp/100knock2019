def cipher(s):
    ans = ""
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            ans += chr(219 - ord(s[i]))
        else:
            ans += s[i]
    return ans
s = "abcdefgABCDEFG"
print(cipher(s))
print(cipher(cipher(s)))
