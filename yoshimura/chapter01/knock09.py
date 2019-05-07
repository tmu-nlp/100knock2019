from random import sample

s = "I couldn't believe that I could actually understand what I was reading \
     : the phenomenal power of the human mind ."

result = []
for w in s.split():
    if len(w) <= 4:
        result.append(w)
    else:
        result.append(w[0] + "".join(sample(w[1:-1], len(w[1:-1]))) + w[-1])

print(" ".join(result))

# random.shuffle()
