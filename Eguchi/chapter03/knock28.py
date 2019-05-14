#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．


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
        temp = re.sub(r"<.*?>\（\）", r"", temp) ##<br />（）
        temp =  re.sub(r"\[.*?\]", r"", temp) ##URL


            
        infodict[line.group("title")] = temp


for i in infodict:
    print("%s: %s" %(i, infodict[i]))