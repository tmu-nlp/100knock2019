import sys

input_file_name = sys.argv[1]
n = int(sys.argv[2])

with open(input_file_name, "r") as input_file:
    for i in range(n):
        print(input_file.readline().strip())
