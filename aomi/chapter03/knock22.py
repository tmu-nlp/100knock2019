import re

with open('jawiki-UK.txt') as UK_file:
    for line in UK_file:
        pattern = '.*\[\[Category:(.*)\]\].*'
        result = re.match(pattern, line)
        if result:
            print(result.group(1))
