with open('col1.txt', 'r') as col1_file, \
     open('col2.txt', 'r') as col2_file, \
     open('col1_2', 'w') as col1_2_file:
     for col1_line, col2_line in zip(col1_file, col2_file):
         col1_line = col1_line.strip()
         col2_line = col2_line.strip()
         print(col1_line + '\t' + col2_line, file = col1_2_file)
