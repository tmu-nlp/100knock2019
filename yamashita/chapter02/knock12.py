import sys

input_file = open(sys.argv[1])
output_file1 = open("col1.txt", "w")
output_file2 = open("col2.txt", "w")

for line in input_file:
    line_list = line.split("\t")

    output_file1.write(line_list[0] + "\n")
    output_file2.write(line_list[1] + "\n")

input_file.close()
output_file1.close()
output_file2.close()
