import re

pattern = re.compile(r'.*?(ファイル|File):(.+?)\|')

with open('jawiki-UK.json', 'r') as UK_file:
    for line in UK_file:
        result = re.search(pattern, line)
        if result:
            print(result.group(2))
