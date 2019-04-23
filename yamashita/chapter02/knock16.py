import sys
import math

input_file_name = sys.argv[1]
n = int(sys.argv[2])
num_line = math.ceil(sum(1 for line in open(input_file_name))/n)


with open(input_file_name, "r") as input_file:
    for i in range(n):
        with open(f"result{i + 1}", "w") as output_file:
            for j in range(num_line):
                line = input_file.readline()
                output_file.write(line)
