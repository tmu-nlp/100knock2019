import json
jawiki_country = open("./jawiki-country.json", "r")
for line in jawiki_country:
    json_line = json.loads(line)
    if "イギリス" in json_line["title"]:
        print (json_line["text"])
