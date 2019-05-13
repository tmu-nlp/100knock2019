import re
import json
import gzip

pattern = re.compile(r'^\|(.+?)\s=\s(.+?)\n', re.MULTILINE + re.DOTALL)

UK_dict  = {}

with gzip.open('jawiki-country.json.gz', 'r') as jawiki_country_file:
    for line in jawiki_country_file:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            for ans in re.findall(pattern, line['text']):
                UK_dict[ans[0]] = ans[1]

for key, value in UK_dict.items():
    print(key + ":" + value)
