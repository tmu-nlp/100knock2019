import gzip
import json
import re


def read_json(filename: str, title: str):
    with gzip.open(filename, "rt", "utf_8") as f:
        for line in f:
            json_data = json.loads(line) #jsonデータを辞書型に変換
            if json_data['title'] == title:
                return json_data['text']


def section(text: str):
    text_list = text.split('\n')
    for line in text_list:
        if re.match(r'=+.*=+', line): # ==地理== level1  ===気候=== level2
            # .+?:非貪欲（以降の条件の巻き込み防止)、この場合.+だと＝も巻き込んでしまう
            s = re.match(r'^(=+)(.+?)=*$', line)
            print('name : {0}   level : {1}'.format(s.group(2), len(s.group(1))-1))


def main():
    text = read_json("jawiki-country.json.gz", "イギリス")
    section(text)


if __name__ == '__main__':
    main()
