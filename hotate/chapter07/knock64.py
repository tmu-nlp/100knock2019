import json
from itertools import islice

import pymongo
from pymongo import MongoClient
from pymongo.cursor import Cursor


class ArtistDB:
    def __init__(self,
                 db_name: str = 'knock64',
                 collection_name: str = 'artist',
                 host: str = 'localhost',
                 port: int = 27017) -> None:
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_artist(self,
                      filename: str = './artist.json',
                      block_size: int = 5000) -> None:
        block = list()
        for i, line in enumerate(open(filename, 'r')):
            artist_dic = json.loads(line)
            block.append(artist_dic)
            if i % block_size == 0:
                self.collection.insert_many(block)
                block = []
        self.collection.insert_many(block)

    def initial_collection(self):
        self.collection.drop()

    def make_index(self):
        self.collection.create_index([('name', pymongo.ASCENDING)])
        self.collection.create_index([('aliases.name', pymongo.ASCENDING)])
        self.collection.create_index([('tags.value', pymongo.ASCENDING)])
        self.collection.create_index([('rating.value', pymongo.ASCENDING)])

    def artist_info(self, name: str) -> Cursor:
        return self.collection.find({"name": name})

    def search_aliases(self, name: str) -> Cursor:
        return self.collection.find({"aliases.name": name})


def main():
    artist_db = ArtistDB()
    artist_db.initial_collection()
    artist_db.insert_artist()
    artist_db.make_index()

    for post in islice(artist_db.collection.find(), 50):
        print(post)


if __name__ == '__main__':
    main()

# mongodb の立ち上げ
# docker-compose up -d

# 終了
# docker-compose stop
