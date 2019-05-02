import sys

with open(sys.argv[1], 'r') as my_file, \
     open('col1.txt', 'w') as col1_file, \
     open('col2.txt', 'w') as col2_file:
    for line in my_file:
        line = line.split('\t')
        print(line[0], file = col1_file)
        print(line[1], file = col2_file)
