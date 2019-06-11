import pymongo
import gzip
import json
from tqdm import tqdm

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.knock64_DB
collection = db.collection_artists

batch = []
i = 0
with gzip.open('artist.json.gz', 'rt', encoding='utf-8') as i_file:
    for line in tqdm(i_file):
        artist = json.loads(line)
        batch.append(artist)
        i += 1
        if i % 100000 == 0 and batch:
            collection.insert_many(batch)
            batch = []

    if batch:
        collection.insert_many(batch)
    print(f'{i}件のデータを格納しました')

for index in ['name', 'alias.name', 'tags.value', 'rating.value']:
    collection.create_index([index, pymongo.ASCENDING])
