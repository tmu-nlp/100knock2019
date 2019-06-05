import json
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.testdb
collection = db.artist

results = collection.find({'tags.value': 'dance'})

results.sort('rating.count', pymongo.DESCENDING)

for result in results[:10]:
    if result.get("rating", "") == "":
        rating = 'no data'
    else:
        rating = result['rating']['count']

    print('{}\tid:{}\t{}'.format(result['name'], result['id'], rating))