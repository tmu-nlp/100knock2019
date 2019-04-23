string1='Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

string1=string1.replace(","," ")
string1=string1.replace("."," ")

words=string1.split()

placefor1=(1,5,6,7,8,9,15,16,19)
dict = {}

key=1
for word in words:
    if key in placefor1:
        dict[word[0]] = key
    else:
        dict[word[:2]] = key
        # dict[word[0]+word[1]] = key
    key+=1

print(dict)
