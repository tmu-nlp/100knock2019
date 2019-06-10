import json
import pymongo
from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)  # 第一引数にはアドレス、第二引数にはポート番号

    # データベースの呼び出し、なかったら自動的に作成される
    db = client.knock64

    # コレクションの呼び出し、RDBでいうとテーブル、なかったら自動的に作成される
    collection = db.artist_info

    # collection.find({'name':'Queen'}) -> <class 'pymongo.cursor.Cursor'>
    for n, value in enumerate(collection.find({'name': 'Queen'}), 1):
        # json.dumps(value, indent=2) はエラー
        # idが特殊な型であるから変換できない、idを削除
        del value["_id"]
        print(f'{n}件目')
        print(json.dumps(value, indent=2) + '\n')

    # インタラクティブシェル db.artist_info.find({name:'Queen'});


if __name__ == '__main__':
    main()

