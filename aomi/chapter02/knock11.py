import sys
my_file = open(sys.argv[1], "r")

for line in my_file:
    line = line.replace('\t', ' ')
    print(line, end = '')

my_file.close()
