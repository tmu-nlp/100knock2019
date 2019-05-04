import re

with open('jawiki-UK.txt') as UK_file:
    pattern = '(=+)(.+?)(=+)'
    for line in UK_file:
        result = re.match(pattern, line)
        if result:
            cnt = len(result.group(1))
            print( " セクション名:" + result.group(2) + " レベル:" + str(cnt - 1))
