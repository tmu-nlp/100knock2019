# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ

from knock20 import get_country_data
from knock25 import extract_basic_info, extract_name_and_value
import requests
import re

def get_national_flag_url(title: str) -> str:
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action" : "query",
        "format" : "json",
        "prop"   : "imageinfo",
        "iiprop" : "url",
        "titles" : "File:{}".format(title.replace(" ", "_"))
    }
    session = requests.Session()
    req = session.get(url=url, params=params)
    res = req.json()
    # res の値から url への path を調べる
    return res["query"]["pages"]["23473560"]["imageinfo"][0]["url"]

if __name__ == "__main__":
    target = get_country_data("イギリス")
    basic_info = extract_basic_info(target)
    title = extract_name_and_value(basic_info)["国旗画像"]
    print(get_national_flag_url(title))