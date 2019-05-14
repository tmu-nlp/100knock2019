import re


with open("jawiki-イギリス.json", "r") as イギリス:
    for line in イギリス:
        category_line = re.search("^\[\[Category:(.*?)(\|.*)*\]\]$", line)
        if category_line is not None:
            print(category_line.group(1))