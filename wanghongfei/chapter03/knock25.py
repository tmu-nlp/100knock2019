import json
import re
jawiki_country = open("./jawiki-country.json", "r")

for line in jawiki_country:
    json_line = json.loads(line)
    if "イギリス" in json_line["title"]:
        uk = json_line["text"]
template_regex = re.compile(r'\|(.*?) =(.*?)\n')
template_info = template_regex.findall(uk)
#extract the basic information
info_dict = {}
for item in template_info:
    info_dict[item[0]] = item[1]
print(info_dict)

