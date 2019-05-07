import random

sentence = input()

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind"

words = sentence.split()
count = 0

for i in words:
    if len(i) >4:
        letterlist = list(i)
        mid = letterlist[1:-1]
        random.shuffle(mid)
        i = letterlist[0]+ ''.join(mid) + letterlist[-1]
        words[count] = i
    count+=1

print(" ".join(words))






       