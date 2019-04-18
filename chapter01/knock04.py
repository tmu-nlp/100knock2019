letter = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

word = letter.split()
ans = []
count = 0

for i in word:
    
    ans.append(word[count][0])
    count+=1


print(ans)