import sys

input_file_name = sys.argv[1]
set_str = set()

with open(input_file_name, "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        line_str = line.split()
        set_str.add(line_str[0])

for s in set_str:
    print(s)
