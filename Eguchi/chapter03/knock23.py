##記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
#https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8

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


for line in sentence:
    line = re.search(r"^(?P<level>=+)(?P<section>.+)\1$", line)
    if line:
        print("%s : %d" %(line.group("section") , line.group("level").count("=")-1 ))
