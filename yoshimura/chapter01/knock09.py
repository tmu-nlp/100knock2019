import random

s = "I couldn't believe that I could actually understand what I was reading \
     : the phenomenal power of the human mind ."

typoglycemia = []
for w in s.split():
    if len(w) <= 4:
        typoglycemia.append(w)
    else:
        random.shuffle(list(w)[1:-1])
        typoglycemia.append(w[0] + w[1:-1] + w[-1])

print(" ".join(typoglycemia))

# random.shuffle()
