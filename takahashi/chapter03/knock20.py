# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import re
import json

def get_country_data(country: str) -> str:
    with open("jawiki-country.json", "r") as file:
        for f in file:
            json_data = json.loads(f)
            if json_data["title"] == country:
                return json_data["text"]

if __name__ == "__main__":
    print(get_country_data("イギリス"))
