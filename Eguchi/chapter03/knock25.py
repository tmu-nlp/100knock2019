#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
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
        infodict[line.group("title")] = line.group("body")

print(infodict)

"""
{{基礎情報 国
|略名 = イギリス
|ISO 3166-1 = GB / GBR
|ccTLD = [[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>
|国際電話番号 = 44
|注記 = <references />
}}


"""