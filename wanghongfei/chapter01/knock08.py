def cipher(x):
    cipher_str = ""
    for alphabet in x:
        if 97 <= ord(alphabet) <= 122:  # ord() can turn the alphabet into number,
            # and chr() can turn the number into alphabet.
            cipher_str += chr(219-ord(alphabet))
        else:
            cipher_str += alphabet
    return cipher_str


x = 'AalkBpD'
print(cipher(x))

