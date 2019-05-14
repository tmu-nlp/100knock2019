import re

with open("jawiki-イギリス.json") as fp:
    json_data = fp.readline()
    while json_data:
        section_line = re.search("^(=+)([^\s=]+)=+$", json_data)
        if section_line is not None:
            print(section_line.group(2), len(section_line.group(1)))
        json_data = fp.readline()
