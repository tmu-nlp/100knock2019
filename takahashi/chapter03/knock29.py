# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ

from knock20 import get_country_data
from knock25 import get_template
import urllib3
import json
import re


def get_national_flag_url(target: str) -> str:
    title = re.sub(" ", "_", get_template(target)["国旗画像"])
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url",
        "titles": f"File:{title}",
    }

    http = urllib3.PoolManager()
    req = http.request("GET", url, fields=params)
    res = json.loads(req.data.decode("utf-8"))

    return res["query"]["pages"]["23473560"]["imageinfo"][0]["url"]


if __name__ == "__main__":
    target = get_country_data("イギリス")
    print(get_national_flag_url(target))
