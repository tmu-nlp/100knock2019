import re

with open('jawiki-UK.txt', 'r') as UK_file:
    pattern = '.*?(ファイル|File):(.+?)\|.*?'
    for line in UK_file:
        result = re.match(pattern, line)
        if result:
            print(result.group(2))
