import json
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["music"]
artists = db["artists"]
with open("/users/hongfeiwang/100knock2019/wanghongfei/chapter07/artist.json", "r") as f:
    for line in f:
        data = json.loads(line)
        artists.insert(data)
artists.create_index([("name", pymongo.ASCENDING)])
artists.create_index([("aliases.name", pymongo.ASCENDING)])
artists.create_index([("tags.value", pymongo.ASCENDING)])
artists.create_index([("rating.value", pymongo.ASCENDING)])