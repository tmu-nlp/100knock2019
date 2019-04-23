import sys

input_file_name = sys.argv[1]

with open(input_file_name, "r") as input_file:
    lines = input_file.readlines()
    lines.sort(key=lambda line: line.split("\t")[2], reverse=True)

for line in lines:
    print(line, end="")

# sort -k 3 -r hightemp.txt
