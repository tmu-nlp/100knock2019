'''
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ:
name, aliases.name, tags.value, rating.value
'''
import sys
import gzip
import json
from pymongo import MongoClient


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


fname = 'artist.json.gz'
db_name = 'artist_db'
collection_name = 'artist_collection'

client = MongoClient('localhost', 27017)
db = client[db_name]                # データベースの呼び出し
collection = db[collection_name]    # データベースの中にあるコレクションの呼び出し
message("[+] connected")

if sum(1 for _ in collection.find()) == 921337:
    message("[*] skip")
else:
    message("[*] make")
    collection.delete_many({})          # collection.drop()
    with gzip.open(fname, "rt") as f:
        collection.insert_many(map(json.loads, f))
    for key in ('name', 'aliases.name', 'tags.value', 'rating.value'):
        collection.create_index(key)

db_size = sum(1 for _ in collection.find())
message(f'[+] {db_name} のサイズ -> {db_size}')


'''
* MongoDB
    - https://www.mongodb.com/
    - https://qiita.com/morrr/items/8bcb5b0fc643267d6bcf
    - https://dackdive.hateblo.jp/entry/2017/08/19/234954
        - brew services start mongodb
        - brew services stop mongodb
* PyMongo
    - http://api.mongodb.com/python/current/api/pymongo/collection.html
    - https://momijiame.tumblr.com/post/116551855651/python-pymongo-%E3%81%A7-mongodb-%E3%82%92%E6%93%8D%E4%BD%9C%E3%81%99%E3%82%8B
* NoSQLデータベース「MongoDB」をPythonで利用する～pymongoの基本的な使い方まとめ～
    - https://qiita.com/ognek/items/a37dd1cd0e26e6adecaa
* JSON形式の概要は以下の通りである．
フィールド	           型	内容	例
id	                  ユニーク識別子	整数	20660
gid	                  グローバル識別子	文字列	"ecf9f3a3-35e9-4c58-acaa-e707fba45060"
name	              アーティスト名	文字列	"Oasis"
sort_name	          アーティスト名（辞書順整列用）	文字列	"Oasis"
area	              活動場所	文字列	"United Kingdom"
aliases	              別名	辞書オブジェクトのリスト
aliases[].name	      別名	文字列	"オアシス"
aliases[].sort_name	  別名（整列用）	文字列	"オアシス"
begin	              活動開始日	辞書
begin.year	          活動開始年	整数	1991
begin.month	          活動開始月	整数
begin.date	          活動開始日	整数
end	                  活動終了日	辞書
end.year	          活動終了年	整数	2009
end.month	          活動終了月	整数	8
end.date	          活動終了日	整数	28
tags	              タグ	辞書オブジェクトのリスト
tags[].count	      タグ付けされた回数	整数	1
tags[].value          タグ内容	文字列	"rock"
rating	              レーティング	辞書オブジェクト
rating.count	      レーティングの投票数	整数	13
rating.value	      レーティングの値（平均値）	整数	86
'''
