
def cipher(str):
    out=''
    for c in str:
        if c.islower():
            out+=chr(219-ord(c))
            print(c)
        else:
            out+=c
    print(out)
    return out

cipher('abc漢字ABCdef')
