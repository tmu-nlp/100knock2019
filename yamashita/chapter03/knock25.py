import sys
import re

pattern = re.compile(r'^\|(.+?)\s=\s(.+?)(?=\n(\||\}))', re.MULTILINE | re.DOTALL)

basic_info = {}
with open(sys.argv[1],'r',encoding='utf-8') as britain_file:
    text = britain_file.read()
    for m in pattern.finditer(text):
        basic_info[m.group(1)] = m.group(2)

print(basic_info)