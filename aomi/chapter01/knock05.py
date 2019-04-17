s = "I am an NLPer"

def n_gram(s, n):
    t = s
    t = t.split(' ')
    word = []
    for i in range(len(t) - n + 1):
        tmp = []
        for j in range(i, i + n):
            tmp.append(t[j])
        word.append(tmp)
    chara = []
    for i in range(len(s) - n + 1):
        tmp = ""
        for j in range(i, i + n):
            tmp += s[j]
        chara.append(tmp)
    return word, chara

ans1, ans2 = n_gram(s, 2)
print(ans1)
print(ans2)
