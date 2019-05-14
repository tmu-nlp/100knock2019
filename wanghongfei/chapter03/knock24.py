import json
import re
jawiki_country = open("./jawiki-country.json", "r")
for line in jawiki_country:
    json_line = json.loads(line)
    if "イギリス" in json_line["title"]:
        uk = json_line["text"]
file_regex = re.compile(r'\[\[(File|ファイル):(.*?\.\w+).*\]\]')
file_name = file_regex.findall(uk)
print(file_name)
