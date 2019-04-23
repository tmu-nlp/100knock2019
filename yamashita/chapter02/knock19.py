import sys

input_file_name = sys.argv[1]
input_file = open(input_file_name, "r")

lines = input_file.readlines()
list_col1 = [line.split("\t")[0] for line in lines]

dic_col1 = {}

for col1 in list_col1:
    if col1 not in dic_col1:
        dic_col1[col1] = 1
    else:
        dic_col1[col1] += 1

for word, c in sorted(dic_col1.items(), key=lambda dic_col1: dic_col1[1], reverse=True):
    print(word.strip(), c)
