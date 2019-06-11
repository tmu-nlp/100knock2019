import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.music
artist_info = db.artists
name = input()
for artist in artist_info.find({"aliases.name":f"{name}"}):
    print(artist)