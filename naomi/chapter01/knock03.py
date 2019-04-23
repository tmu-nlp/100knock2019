import re
str='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

words=re.split('[ ,.]',str)


list=[]

for word in words:
    if len(word)!=0:
        list.append(len(word))

print(list)
