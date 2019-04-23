import re
import random

def Typoglycemia(str):
    str_list = re.split('[ ]',str)
    str_list = [x for x in str_list if x is not ""]

    rand_list = []
    for i in str_list:
        if len(i) > 3:
            j = list(i[1:len(i)-1])
            random.shuffle(j)
            rand_list.append(i[0]+''.join(j)+i[len(i)-1])
        else:
            rand_list.append(i)

    return rand_list

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

rand_list = Typoglycemia(str)

print(str)
# print(x)
print(' '.join(rand_list))
