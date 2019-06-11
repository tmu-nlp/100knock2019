'''
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．さらに，これと同様の処理を行うプログラムを実装せよ．
'''

import json
import sys
from pymongo import MongoClient


# def MongoDB_find(json_path: str, name: str):
#     with open(json_path) as f:
#         for line in f:
#             json_Data = json.loads(line)
#             if json_Data["name"] == "Queen":
#                 print(json_Data)


# if __name__ == "__main__":
#     json_path = "artist.json"
#     MongoDB_find(json_path, " ".join(sys.argv[1:]))


client = MongoClient()
db = client.artist_database
collection = db.artist_collection
for doc in collection.find({"name": "Queen"}):
    print(doc)


'''
> show dbs
admin            0.000GB
artist_database  0.252GB
config           0.000GB
local            0.000GB
test_database    0.000GB
> use artist_database
switched to db artist_database
> db
artist_database
> show collections
artist_collection
> db.artist_collection.find( {name:'Queen'} )
{ "_id" : ObjectId("5cfca25a6e18fb7438894d0d"), "name" : "Queen", "area" : "Japan", "gender" : "Female", "tags" : [ { "count" : 1, "value" : "kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
{ "_id" : ObjectId("5cfca26d6e18fb74388a13b9"), "rating" : { "count" : 24, "value" : 92 }, "begin" : { "date" : 27, "month" : 6, "year" : 1970 }, "name" : "Queen", "area" : "United Kingdom", "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "sort_name" : "Queen", "ended" : true, "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "type" : "Group", "id" : 192, "aliases" : [ { "name" : "女王", "sort_name" : "女王" } ] }
{ "_id" : ObjectId("5cfca29b6e18fb74388bce11"), "ended" : true, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen", "id" : 992994, "name" : "Queen" }
{ "_id" : ObjectId("5cfcaa95e64b561e1d91fa65"), "name" : "Queen", "area" : "Japan", "gender" : "Female", "tags" : [ { "count" : 1, "value" : "kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
{ "_id" : ObjectId("5cfcaab5e64b561e1d92c111"), "rating" : { "count" : 24, "value" : 92 }, "begin" : { "date" : 27, "month" : 6, "year" : 1970 }, "name" : "Queen", "area" : "United Kingdom", "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "sort_name" : "Queen", "ended" : true, "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "type" : "Group", "id" : 192, "aliases" : [ { "name" : "女王", "sort_name" : "女王" } ] }
{ "_id" : ObjectId("5cfcaaf3e64b561e1d947b69"), "ended" : true, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen", "id" : 992994, "name" : "Queen" }
'''
