import gzip
import json


def search (filename, keyword):
    with gzip.open( filename,'rt',encoding="utf-8") as opendedfile:
        for line in opendedfile:
            filedict = json.loads(line)

            if (filedict["title"] == keyword):
                return filedict["text"]


filename=r"\Users\Koya\Documents\Lab\jawiki-country.json.gz"
print(search(filename, "イギリス"))

