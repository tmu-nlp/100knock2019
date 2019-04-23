import sys

input_file_name = sys.argv[1]

with open(input_file_name, "r") as input_file:
    f = input_file.read()
    result = f.replace("\t", " ")

print(result)
