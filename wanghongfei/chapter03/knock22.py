import re
import json
jawiki_country = open("./jawiki-country.json", "r")
for line in jawiki_country:
    json_line = json.loads(line)
    if "イギリス" in json_line["title"]:
        uk = json_line["text"]
category_regex = re.compile(r'\[\[Category:.*]]')
category_name = category_regex.findall(uk)
print(category_name)

