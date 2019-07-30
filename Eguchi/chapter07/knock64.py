#アーティスト情報（artist.json.gz）をデータベースに登録せよ．
# さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
import gzip
import json
import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.testdb
collection = db.artist


def reg(collection):
    collection.remove()
    path =r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter07\artist.json"
    datalist = []
    unit = 10000 
    with open(path, mode="r", encoding= "utf-8") as f:
        for i, line in enumerate(f) :
            json_line = json.loads(line)
            datalist.append(json_line)

            if i % unit == 0:
                collection.insert_many(datalist)
                datalist = []
                print("%d件登録" %i)

        if len(datalist) > 0:
            collection.insert_many(datalist)
            print("%d件登録" %i)


    collection.create_index([('name', pymongo.ASCENDING)])  
    collection.create_index([('aliases.name', pymongo.ASCENDING)])  
    collection.create_index([('tags.value', pymongo.ASCENDING)])
    collection.create_index([('rating.value', pymongo.ASCENDING)])

reg(collection)
