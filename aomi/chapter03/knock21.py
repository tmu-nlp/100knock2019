import re

with open('jawiki-UK.txt') as UK_file:
    pattern = '.*(\[\[Category:.*\]\]).*'
    for line in UK_file:
        result = re.match(pattern, line)
        if result:
            print(result.group())
