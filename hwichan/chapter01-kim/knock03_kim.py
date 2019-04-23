import re
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list1 = re.split('[., ]',str)
list2 = [x for x in list1 if x is not ""]

list3 = []
for i in list2:
    list3.append(len(i))

print(list1)
print(list2)
print(list3)
