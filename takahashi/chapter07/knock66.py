# 66. 検索件数の取得
# MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．

"""
> show dbs
admin         0.000GB
config        0.000GB
gg            0.000GB
local         0.000GB
nlp100_knock  0.160GB

> use nlp100_knock
switched to db nlp100_knock

> show collections
artists

> db.artists.find({"area": "Japan"}).count()
23425
"""
