#記事中でカテゴリ名を宣言している行を抽出せよ．

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
    if "Category" in line:
        print(line)
