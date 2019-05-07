import re

#文字
def n_gram1(str,num):
    list = []
    for i in range(len(str)-num+1): #iは一文字ずつ増えていくため、前の配列の最終文字も含めるから
        list.append(str[i:i+num])

    return list

#単語
def n_gram2(str,num):
    list1 = re.split('[., ]',str)
    list2 = [x for x in list1 if x is not ""]

    list = []
    for i in range(len(list2)-num+1):
        list3 = []
        for j in range(num):
            list3.append(list2[i+j]) # list2は単語の配列であるからiで最初の単語を決めてj(0 ~ num-1)を足して単語を追加

        list.append(list3)

    return list

str = "I am an NLPer"

print(str)
print(n_gram1(str,2))
print(n_gram2(str,2))
