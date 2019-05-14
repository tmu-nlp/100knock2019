from django.db import models
from pymongo import MongoClient
import pymongo
import json


class ArtistDB:
    def __init__(self, db_name='knock64', collection_name='artist'):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_artist(self, filename='./artist.json', block_size=5000):
        block = list()
        for i, line in enumerate(open(filename, 'r')):
            artist_dic = json.loads(line)
            block.append(artist_dic)
            if i % block_size == 0:
                self.collection.insert_many(block)
                block = []
        self.collection.insert_many(block)

    def make_index(self):
        self.collection.create_index([('name', pymongo.ASCENDING)])
        self.collection.create_index([('aliases.name', pymongo.ASCENDING)])
        self.collection.create_index([('tags.value', pymongo.ASCENDING)])
        self.collection.create_index([('rating.value', pymongo.ASCENDING)])

    def search_artist(self, name, limit):
        for post in self.collection.find({"name": name}).sort([("rating.count", -1)]).limit(limit):
            yield post

    def search_area(self, area, limit):
        for post in self.collection.find({"area": area}).sort([("rating.count", -1)]).limit(limit):
            yield post

    def search_aliases_name(self, name, limit):
        for post in self.collection.find({"aliases.name": name}).sort([("rating.count", -1)]).limit(limit):
            yield post

    def search_tag(self, tag, limit):
        for rank in self.collection.find({"tags.value": tag}).sort([("rating.count", -1)]).limit(limit):
            yield rank
