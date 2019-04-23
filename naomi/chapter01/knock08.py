
def cipher(str):
    out=''
    i=0
    for c in str:
        if c.islower():
            out+=chr(219-ord(str[i]))
            print(str[i])
        else:
            out+=str[i]
        i+=1
    print(out)
    return out

cipher('abc漢字ABCdef')
