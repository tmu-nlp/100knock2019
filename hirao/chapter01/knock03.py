s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
drop = ",."
print(s)
for c in list(drop):
    s = s.replace(c, "")
s = s.split()
print(s)


def count_letter(word):
    return len(word)


s = list(map(count_letter, s))
print(s)
