
import gzip
import json
import re
import requests



def search (filename, keyword):
    with gzip.open( filename,'rt',encoding="utf-8") as opendedfile:
        for line in opendedfile:
            filedict = json.loads(line)

            if (filedict["title"] == keyword):
                return filedict["text"]



filename=r"\Users\Koya\Documents\Lab\jawiki-country.json.gz"

sentence = search(filename, "イギリス").split("\n")

infodict = {}
temp=""

for line in sentence:
    line = re.search("^\|(?P<title>.*?)\s=\s(?P<body>.*)", line)
    
    if line:
        temp = re.sub(r"'{2,5}", r"", line.group("body"))
        temp = re.sub(r"\[\[([^]]+)\]\]", r"", temp)
        temp = re.sub(r"<.*?>\（\）", r"", temp) ##<br />（）
        temp =  re.sub(r"\[.*?\]", r"", temp) ##URL
        infodict[line.group("title")] = temp


for i in infodict:
    print("%s: %s" %(i, infodict[i]))

def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    return ret_dict


#Flag of the United Kingdom.svg


url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(infodict[u"国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

json_data = requests.get(url, params=payload).json()

print(json_search(json_data)["url"])