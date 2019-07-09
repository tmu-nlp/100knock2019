#MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．

from tqdm import tqdm
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.testdb
collection = db.artist

count = collection.find({"area":"Japan"}).count()
print(count)