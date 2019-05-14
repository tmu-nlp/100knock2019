import gzip
import json


def read_json(filename: str, title: str):
    with gzip.open(filename, "rt", "utf_8") as f:
        for line in f:
            json_data = json.loads(line)  # jsonデータを辞書型に変換
            if json_data['title'] == title:  # json_dataの'title'キーに記事名、'text'キーに記事本文が格納
                return json_data['text']


def main():
    text = read_json("jawiki-country.json.gz", "イギリス")
    print(text)


if __name__ == '__main__':
    main()
