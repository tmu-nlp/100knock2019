# 64. MongoDBの構築
# アーティスト情報（artist.json.gz）をデータベースに登録せよ．
# さらに，次のフィールドでインデックスを作成せよ:
# name, aliases.name, tags.value, rating.value

import json
import gzip
from pymongo import MongoClient
import pymongo


def save_db_mongo(path: str):

    client = MongoClient('localhost', 27017)

    # DBの呼び出し（なかったら作る）
    db = client['64mongo']

    # Collectionの呼び出し（なかったら作る）
    collection = db['64mongo-collection']

    with gzip.open(path, 'rt', encoding='utf-8') as f:
        # insert_oneでなくinsert_manyを使うためのバッチ
        artists = []
        for i, line in enumerate(f):
            # Jsonファイルからデータのとりだし
            artist = json.loads(line)
            # バッチに追加
            artists.append(artist)

            # 10000個ずつDBに登録
            if not i % 10000 and artists:
                collection.insert_many(artists)
                artists = []

        # Indexつける
        collection.create_index([('name', pymongo.ASCENDING)])
        collection.create_index([('aliases.name', pymongo.ASCENDING)])
        collection.create_index([('tags.value', pymongo.ASCENDING)])
        collection.create_index([('rating.value', pymongo.ASCENDING)])


def main():
    path = 'artist.json.gz'
    save_db_mongo(path)


if __name__ == '__main__':
    main()
