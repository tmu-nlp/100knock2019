import re
import json
import gzip

#テンプレートの抽出
pattern = re.compile(r'^\|(.+?)\s=\s(.+?)(\n)', re.MULTILINE + re.DOTALL)

#強調マークアップの除去
pattern2 = re.compile(r'\'{2,5}', re.MULTILINE + re.DOTALL)

#内部リンクの除去
#[[記事名]]->記事名, [[記事名|表示文字]]->表示文字, [[記事名#節名|表示文字]]->表示文字
pattern3 = re.compile(r'\[{2}(?:[^|]*?\|)*?([^|]*?)\]{2}', re.MULTILINE + re.DOTALL)

#{{lang|言語タグ|文字列}}->文字列
pattern4 = re.compile(r'\{\{lang(?:[^|]*?\|)([^|]*?)\}\}', re.MULTILINE + re.DOTALL)

#<br>, <ref> , </br>, </ref>の除去
pattern5 = re.compile(r'<\/?[br|ref](.*?)>', re.MULTILINE + re.DOTALL)

UK_dict  = {}

with gzip.open('jawiki-country.json.gz', 'r') as jawiki_country_file:
    for line in jawiki_country_file:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            for ans in pattern.finditer(line['text']):
                ans2 = pattern2.sub("", ans.group(2))
                ans2 = pattern3.sub(r'\1', ans2)
                ans2 = pattern4.sub(r'\1', ans2)
                ans2 = pattern5.sub('', ans2)
                UK_dict[ans.group(1)] = ans2

for key, value in UK_dict.items():
    print(key + ":" + value)
