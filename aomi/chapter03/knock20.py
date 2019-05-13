import json
import gzip

with gzip.open('jawiki-country.json.gz', 'r') as jawiki_country_file,\
     open('jawiki-UK.json', 'wt') as UK_file
    for line in jawiki_country_file:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            print(line['text'], file=UK_file)
