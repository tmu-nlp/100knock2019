import json
import re
jawiki_country = open("./jawiki-country.json", "r")
for line in jawiki_country:
    json_line = json.loads(line)
    if "イギリス" in json_line["title"]:
        uk = json_line["text"]
section_regex = re.compile(r'={2}.*={2}')
section_name = section_regex.findall(uk)
section_level = {}
for section in section_name:
    count = 0
    for item in section:
        if item == "=":
                count += 1
    section_level[section] = int(count / 2) - 1
    count = 0
print(section_level)

