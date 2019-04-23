sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list_number = [1, 5, 6, 7, 8, 9, 15, 16, 19, 1]
sentence_edit = sentence.replace('.', '')
words = sentence_edit.split(' ')
dic = {}
count = 0
for i in range(len(words)):
    if list_number[count] == i + 1:
        dic[words[i][0]] = i + 1
        count += 1
    else:
        dic[words[i][0:2]] = i + 1
print(dic)