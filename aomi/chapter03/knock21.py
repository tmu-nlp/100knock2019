import re

pattern = re.compile(r'.*(\[\[Category:.*\]\]).*')

with open('jawiki-UK.json') as UK_file:
    for line in UK_file:
        result = re.match(pattern, line)
        if result:
            print(result.group())
