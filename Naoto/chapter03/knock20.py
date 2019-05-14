import json


with open("jawiki-country.json") as f, open("jawiki-イギリス.json", mode="w") as イギリス:
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == "イギリス":
            イギリス.write(article_dict["text"])
        article_json = f.readline()