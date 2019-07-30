#特定の（指定した）別名を持つアーティストを検索せよ．


from tqdm import tqdm
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.testdb
collection = db.artist
key = input("別名を入力--->")

alias_name = collection.find({"aliases.name":key})

for i, data in enumerate( alias_name, start=1):
    print("%d件目\n%s" %(i, data))

