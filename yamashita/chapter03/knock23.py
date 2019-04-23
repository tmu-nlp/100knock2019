import sys
import re

with open(sys.argv[1],'r',encoding='utf-8') as britain_file:
    for line in britain_file:
        m = re.match(r'(=+)([^=]*)=+', line)
        if m: print(m.group(2) + ' レベル：{}'.format(len(m.group(1))-1))
