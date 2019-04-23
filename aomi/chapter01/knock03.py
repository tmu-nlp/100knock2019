s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(',', '')
s = s.replace('.', '')
s = s.split(' ')
ans = []
for i in s:
    ans.append(len(i))
print(ans)
