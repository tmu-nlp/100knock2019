from pymongo import MongoClient

client = MongoClient()
db = client.music
artist_info = db.artists

for data in artist_info.find({"name":"Queen"}):
    print(data)
