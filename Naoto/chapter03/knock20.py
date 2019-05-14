import json


count = 0
with open("jawiki-country.json") as f, open("jawiki-イギリス.json", mode="w") as イギリス:
    article_json = f.readline()
    if count == 0:
        # print(type(article_json))
        count += 1
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == u"イギリス":
            イギリス.write(article_dict["text"])
        article_json = f.readline()