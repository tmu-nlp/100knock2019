#"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
import json
from pymongo import MongoClient
from tqdm import tqdm
from pymongo
import json
from bson.objectid import ObjectId

client = MongoClient()
db = client.testdb
collection = db.artist

ans = collection.find({"tag.value": "dance"})
ans.sort("rating.count", pymongo.DESCENDING)

for i, va in enumerate(ans):
    if "rating" in va:
        rating = va["rating"]["count"]

    else:
        rating="(none)"
    print("{} (ID: {}) \t {}" .format(va["name"], doc["id"], rating))
    
    if i > 10:
        break
        