import sys

input_file_name = sys.argv[1]
n = int(sys.argv[2])

with open(input_file_name, "r") as input_file:
    line_list = input_file.readlines()
    for line in line_list[-n:]:
        print(line.strip())
