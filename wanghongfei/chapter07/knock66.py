import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.music
artist_info = db.artists
count = artist_info.find({"area":"Japan"}).count()
print(count)