import re

pattern = re.compile(r'(=+)(.+?)\1')

with open('jawiki-UK.json') as UK_file:
    for line in UK_file:
        result = re.match(pattern, line)
        if result:
            cnt = len(result.group(1))
            print( " セクション名:" + result.group(2) + " レベル:" + str(cnt - 1))
