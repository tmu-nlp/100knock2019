import json
import re

jawiki_country = open("./jawiki-country.json", "r")
for line in jawiki_country:
    json_line = json.loads(line)
    if "イギリス" in json_line["title"]:
        uk = json_line["text"]
template_regex = re.compile(r'\|(.*?) =(.*?)\n')
template_info = template_regex.findall(uk)

info_dict = {}
del_highlight = re.compile(r"'{2}(.*)'{2}")
del_link = re.compile(r"\[\[(.*?)\]\]")
for item in template_info:
    info_dict[item[0]] = del_highlight.sub(r'\1',del_link.sub(r'\1',item[1]))
# delete '' '' and [[ ]]
print(info_dict)


