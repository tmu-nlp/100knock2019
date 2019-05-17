#25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ


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
for line in sentence:
    line = re.search("^\|(?P<title>.*?)\s=\s(?P<body>.*)", line)
    
    if line:
        infodict[line.group("title")] = re.sub(r"'{2,5}", r"", line.group("body"))


print(infodict)

