'''
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
'''
import re

from knock25 import template_extract
from knock26 import Highlight_markup_removal
from knock27 import inner_link_removal
from knock28 import MediaWiki_markup_removal


import gzip
import json
import re
import urllib.parse, urllib.request


def get_country_flag(s: str) -> str:
    import requests
    # S = requests.Session()
    # URL = "https://ja.wikipedia.org/w/api.php"
    # PARAMS = {
    #     "action":"query",
    #     "format":"json",
    #     "prop": "imageinfo",
    #     "titles": s,
    # }
    # R = S.get(url=URL, params=PARAMS)
    # print(type(R))
    # print(R)
    # print(R.json())
    # DATA = R.json()
    # print(type(DATA))
    # print(DATA)
    url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(s)\
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

    # MediaWikiのサービスへリクエスト送信
    request = urllib.request.Request(url)
    print(request)
    print(type(request))
    connection = urllib.request.urlopen(request)
    print(connection)
    print(type(connection))

    # jsonとして受信
    data = json.loads(connection.read().decode())
    print(data)

    # URL取り出し
    url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
    print(url)


if __name__ == "__main__":
    input_file = "jawiki-イギリス.json"
    dic_ = template_extract(input_file)
    dic_markup_removal = Highlight_markup_removal(dic_)
    dic_inner_link_removal = inner_link_removal(dic_markup_removal)
    dic_media_wiki_marckup_removal = MediaWiki_markup_removal(dic_inner_link_removal)
    get_country_flag(dic_media_wiki_marckup_removal["国旗画像"])
    # print(url)