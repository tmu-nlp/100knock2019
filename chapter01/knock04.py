letter = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

word = letter.split()
ans = []
 
for i in range(15):
    ans.append(word[i][0])

print(ans)