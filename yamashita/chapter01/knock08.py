def cipher(s):
    result = ""
    for c in s:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c

    return result


if __name__ == "__main__":
    s = "I am a NLPer"
    print(cipher(s))
    print(cipher(cipher(s)))
