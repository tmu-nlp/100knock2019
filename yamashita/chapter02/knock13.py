
input_file1 = open("col1.txt")
input_file2 = open("col2.txt")
output_file = open("result.txt", "w")

for line1, line2 in zip(input_file1, input_file2):
    output_file.write(line1.strip() + "\t" + line2)

input_file1.close()
input_file2.close()
output_file.close()
