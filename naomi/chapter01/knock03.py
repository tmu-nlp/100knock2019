import re
string1='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
string1 = string1.replace(',', '')
string1 = string1.replace('.', '')
words=re.split(' ',string1)


list=[]

for word in words:
    if len(word)!=0:
        list.append(len(word))

print(list)
