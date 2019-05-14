import gzip
import requests
from knock20 import jsons2dict
from knock28 import exttemplate


def geturl_flagimg(d: dict) -> str:

    S = requests.Session()

    URL = "https://ja.wikipedia.org/wiki/api.php"
    URL = "https://ja.wikipedia.org/w/api.php"

    title = d['国旗画像']

    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": title,
    }

    R = S.get(url=URL, params=PARAMS)
    return R.url


def main():
    with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8') as fs:

        data = jsons2dict(fs, 'イギリス')
        template = exttemplate(data['text'])
        url = geturl_flagimg(template)
        print(url)
    return None


if __name__ == '__main__':
    main()
