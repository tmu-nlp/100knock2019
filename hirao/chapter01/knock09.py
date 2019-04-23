import random
random.seed(0)
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def swap_string(s):
    output = list(s)
    if len(s) > 4:
        indexs = list(range(1, len(s)-1))
        random.shuffle(indexs)
        for i, shuffled_index in enumerate(indexs):
            output[1+i] = s[shuffled_index]
    return "".join(output)

ans = ""
for word in s.split():
    ans += swap_string(word) + " "
print(ans)
