import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
s = s.split(' ')
ans = []
for word in s:
    if len(word) <= 4:
        ans.append(word)
    else:
        t = []
        for i in range(1, len(word) - 1):
            t.append(word[i])
        random.shuffle(t)
        t = word[0] + ''.join(t) + word[len(word) - 1]
        ans.append(t)
ans = ' '.join(ans)
print (ans)
