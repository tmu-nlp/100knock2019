'''
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）．
'''
import re
import sys
import json
import pprint
import requests
import urllib.request
import urllib.parse
from knock25 import extract_infobox


def fetch_url_of_national_flag_by_requests(fname):
    S = requests.Session()
    URL = "https://www.mediawiki.org/w/api.php"
    PARAMS = {
        "action": "query",
        "titles": f"File:{fname}",
        "prop": "imageinfo",
        "format": "json",
        "iiprop": "url",
    }
    return S.get(url=URL, params=PARAMS).json()


def fetch_url_of_national_flag(fname):
    params = urllib.parse.urlencode({
        'action': "query",
        'titles': f"File:{fname}",
        'prop': "imageinfo",
        'format': "json",
        'iiprop': "url",
    })
    url = "https://www.mediawiki.org/w/api.php?%s" % params
    with urllib.request.urlopen(url) as f:
        data = json.loads(f.read().decode('utf-8'))
    return data


def fetch_img_of_national_flag(url, fname):
    with urllib.request.urlopen(url) as f_img:
        raw_img = f_img.read()
        with open(fname, 'wb') as f_out:
            f_out.write(raw_img)


def check(fname):
    import webbrowser
    contents = '''<!DOCTYPE html><html>
<head><meta charset="utf-8"/><title></title></head>
<body><img src="%s" width="128"/></body>
</html>''' % fname
    with open('out29.html', 'w') as f:
        print(contents, file=f)
    webbrowser.open('out29.html')


if __name__ == '__main__':
    fname = extract_infobox()['国旗画像']
    data = fetch_url_of_national_flag(fname)
    assert data == fetch_url_of_national_flag_by_requests(fname)
    pprint.pprint(data, stream=sys.stderr)
    url = data['query']['pages']['-1']['imageinfo'][0]['url']
    fetch_img_of_national_flag(url, fname)
    check(fname)


''' NOTE
* MediaWiki API
-> https://www.mediawiki.org/wiki/API:Main_page/ja

* imageinfo
-> https://www.mediawiki.org/wiki/API:Properties/ja#imageinfo_.2F_ii

* urllib.request --- URL を開くための拡張可能なライブラリ
-> https://docs.python.org/ja/3/library/urllib.request.html
'''
