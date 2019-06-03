import re
import sys

path = sys.argv[1]
newline = re.compile(r'^\n', re.MULTILINE)
pattern = re.compile(r'([.;:?!])\s([A-Z])', re.MULTILINE)
with open(path, 'r', encoding='utf-8') as i_file:
    with open('result_50.txt', 'w', encoding='utf-8') as o_file:
        txt = newline.sub('', i_file.read())
        matches = pattern.finditer(txt)
        for match in matches:
            print(pattern.sub(r'\1\n\2', txt), file=o_file)
