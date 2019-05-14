#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ

import gzip
import json
import re


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
        infodict[line.group("title")] = temp


for k, v in sorted(infodict.items(), key=lambda x: x[0]):
    print(k, v)
