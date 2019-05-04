import re

with open('jawiki-UK.txt') as UK_file:
    pattern = '(=+)(.*)=+'
    for line in UK_file:
        result = re.match(pattern, line)
        if result:
            cnt = len(result.group(1))
            print(result.group(), end = '')
            print(cnt - 1)
