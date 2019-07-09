#MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
# さらに，これと同様の処理を行うプログラムを実装せよ．

from tqdm import tqdm
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.testdb
collection = db.artist


for i, word in enumerate( collection.find({"name":"Queen"})):
    print("%d件目" %i)
    print(word)
