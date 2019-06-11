'''
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．\
    さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
'''


from pymongo import MongoClient, IndexModel, ASCENDING, DESCENDING
import json


def MongoDB_built(json_path):
    client = MongoClient()
    # client = MongoClient('mongodb://localhost:27017/')  # URLで指定
    db = client.artist_database
    collection = db.artist_collection
    # collection = db['test-collection']

    # with open(json_path) as f:  # データ構築
    #     for i, line in enumerate(f):
    #         json_Data = json.loads(line)
    #         collection.insert_one(json_Data)

    # for i, post in enumerate(collection.find()):
    #     if i > 5:
    #         break
    #     print(post)

    collection.create_index([("tags.value", ASCENDING), ("rating.value", DESCENDING)])


if __name__ == "__main__":
    json_path = "artist.json"
    MongoDB_built(json_path)
