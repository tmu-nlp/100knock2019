import gzip
import json
import pymongo
from pymongo import MongoClient

file_name = "artist.json.gz"
unit_bulk = 10000

# sudo mongod --dbpath /var/lib/mongodb --logpath /var/log/mongodb.log
client = MongoClient()
db = client.testdb
collection = db.artist

with gzip.open(file_name) as data_file:
    buf = []
    for i, line in enumerate(data_file, 1):
        data_json = json.loads(line)
        buf.append(data_json)

        # unit_bulk件たまったらartistへバルクインサート
        if i % unit_bulk == 0:
            collection.insert_many(buf)
            buf = []
            print('{}件追加完了'.format(i))

    # 最後のunit_bulkに入らなかった半端分の追加
    if len(buf) > 0:
        collection.insert_many(buf)
        print('{}件追加完了'.format(i))

# インデックス作成
collection.create_index([('name', pymongo.ASCENDING)])  
collection.create_index([('aliases.name', pymongo.ASCENDING)])  
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])