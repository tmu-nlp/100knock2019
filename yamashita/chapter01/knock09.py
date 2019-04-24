import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = s.split(" ")
result = []
for w in words:
    if len(w) > 4:
        chr_list = list(w[1:-1])
        random.shuffle(chr_list)
        w = w[0] + "".join(chr_list) + w[-1]
    result.append(w)

print(" ".join(result))
