import gzip
import json
import pymongo
from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)  # 第一引数にはアドレス、第二引数にはポート番号

    # データベースの呼び出し、なかったら自動的に作成される
    db = client.knock64

    # コレクションの呼び出し、RDBでいうとテーブル、なかったら自動的に作成される
    collection = db.artist_info

    insert_list = []  # テーブルに追加するデータを格納
    with gzip.open('artist.json.gz') as f:
        for n, line in enumerate(f, 1):
            json_data = json.loads(line)
            insert_list.append(json_data)

        collection.insert_many(insert_list)
        print(f'{n}件追加しました')

    collection.create_index([('name', pymongo.ASCENDING)])
    collection.create_index([('aliases.name', pymongo.ASCENDING)])
    collection.create_index([('tags.value', pymongo.ASCENDING)])
    collection.create_index([('rating.value', pymongo.ASCENDING)])


if __name__ == '__main__':
    main()

