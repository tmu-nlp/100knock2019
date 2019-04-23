def cipher(s: str) -> str:
    return ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s)

Apple_commercial = 'And you\'ll se why 1984 won\'t be like 1984'
print(cipher(Apple_commercial))
print(cipher(cipher(Apple_commercial)))
