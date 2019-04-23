import re
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list1 = re.split('[., ]',str) # []の中の区切り文字により分割
list2 = [x for x in list1 if x is not ""] #そのままだと空文字が配列の中に入ってしまうから空文字削除

list3 = []
for i in list2:
    list3.append(len(i))

print(list1) #空文字入り配列
print(list2) #空文字削除配列
print(list3) #文字数配列
