# 64. MongoDBの構築
# アーティスト情報（artist.json.gz）をデータベースに登録せよ．
# さらに，次のフィールドでインデックスを作成せよ:
#   name, aliases.name, tags.value, rating.value

from pymongo import MongoClient, ASCENDING
import gzip
import json


def init():
    client = MongoClient("localhost", 27017)
    db = client.nlp100_knock
    col = db.artists

    i = 0
    pipeline = []
    for line in gzip.open("../data/artist.json.gz", "rt", encoding="utf-8"):
        artist = json.loads(line)
        pipeline.append(artist)
        i += 1
        if i % 100000 == 0 and pipeline:
            col.insert_many(pipeline)
            pipeline = []

    if pipeline != []:
        col.insert_many(pipeline)
    print(f"stored {i} items")

    for index in ["name", "aliases.name", "tags.value", "rating.value"]:
        col.create_index([(index, ASCENDING)])


if __name__ == "__main__":
    init()
