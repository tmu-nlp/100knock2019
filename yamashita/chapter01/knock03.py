s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = s.split()
ans = []
for word in words:
    ans.append(len(word.strip(".,")))

print(ans)
