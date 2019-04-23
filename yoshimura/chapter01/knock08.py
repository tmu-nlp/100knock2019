
def cipher(s: str):
    result = ""
    for c in s:
        if c.lower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result


if __name__ == "__main__":
    s = "I am a NLPer"
    print(cipher(s))  # 暗号化
    print(cipher(cipher(s)))  # 復号化

# ord : 文字 → ASCII 
# chr : ASCII → 文字