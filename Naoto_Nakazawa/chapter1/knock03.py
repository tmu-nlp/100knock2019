import string
pi = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
pi_edit = pi.replace(',', '')
pi_edit = pi_edit.replace('.', '')
words_pi = pi_edit.split(' ')
ans = []
for i in range(len(words_pi)):
    ans.append(len(words_pi[i]))
print(ans)