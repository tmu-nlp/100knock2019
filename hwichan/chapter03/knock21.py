import gzip
import json
import re


def read_json(filename: str, title: str):
    with gzip.open(filename, "rt", "utf_8") as f:
        for line in f:
            json_data = json.loads(line)  # jsonデータを辞書型に変換
            if json_data['title'] == title:
                return json_data['text']


def category(text: str):
    text_list = text.split('\n')
    for line in text_list:
        if re.match(r'.*Category:', line):  # . 任意の文字列  * 0回以上の繰り返し
            print(line)


def main():
    text = read_json("jawiki-country.json.gz", "イギリス")
    category(text)


if __name__ == '__main__':
    main()
