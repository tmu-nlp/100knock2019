import re
from json import loads

with open('jawiki-country.json', 'r') as jawiki_country_file, \
     open('jawiki-UK.txt', 'w') as jawiki_UK_file:
    for line in jawiki_country_file:
        line = loads(line)
        if line['title'] == 'イギリス':
            print(line['text'], file = jawiki_UK_file)
