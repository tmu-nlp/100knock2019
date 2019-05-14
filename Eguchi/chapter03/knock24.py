#記事から参照されているメディアファイルをすべて抜き出せ．

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

#[[ファイル:The Fabs.JPG|thumb|200px|[[ビートルズ]]]]

for line in sentence:
    line = re.search("ファイル:(?P<filetitle>[^|]+)\|", line)
    if line:
        print(line.group("filetitle"))

