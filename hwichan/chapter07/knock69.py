#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import pymongo
from pymongo import MongoClient


# python -m http.server --cgi
# http://localhost:8000/

client = MongoClient('localhost', 27017)  # 第一引数にはアドレス、第二引数にはポート番号

# データベースの呼び出し、なかったら自動的に作成される
db = client.knock64

# コレクションの呼び出し、RDBでいうとテーブル、なかったら自動的に作成される
collection = db.artist_info

form = cgi.FieldStorage()
name = form.getvalue('name', '')
aliases_name = form.getvalue('aliases.name', '')
tags = form.getvalue('tags', '')

search_list = []
if name is not '':
    search_list.append({'name': name})

if aliases_name is not '':
    search_list.append({'aliases.name': aliases_name})

if tags is not '':
    search_list.append({'tags.value': tags})
search_info = collection.find({"$and": search_list}).sort('rating.count', pymongo.DESCENDING)

start = """
<!DOCTYPE html>
<html>
    <head>
        <title>knock69</title>
        <meta charset="utf-8"/>
        <style>
        h1 {
        font-size: 3em;
        }
        </style>
    </head>
    <body>
"""

artist_info = ""
for n, value in enumerate(search_info):

    # 別名の取得
    if 'aliases' in value:
        aliases_name = value['aliases'][0]['name']
    else:
        aliases_name = '不明'

    # tagの取得
    tags = []
    if 'tags' in value:
        for tag in value['tags']:
            tags.append(f"{tag['value']}")

    # rationg
    if 'rating' in value:
        rating = value['rating']['count']
    else:
        rating = '投票数なし'

    artist_info += f"名前 : {value['name']} <br/> \
                     別名 :  {aliases_name} <br/> \
                     地域 : {value.get('area', '不明')} <br/> \
                     レーティング : {rating} <br/> \
                     タグ : {', '.join(tags)} <br/> <hr />"

end = """
    </body>
</html>
"""

print(start + artist_info + end)
