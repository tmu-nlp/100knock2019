import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.music
artist_info = db.artists
dance = artist_info.find({"tags.value":"dance"}).sort("rating.count",pymongo.DESCENDING)
for i in dance[0:10]:
    print(i["name"], i["rating"]["count"])