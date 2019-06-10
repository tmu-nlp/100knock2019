import json
import pymongo
from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)  # 第一引数にはアドレス、第二引数にはポート番号

    # データベースの呼び出し、なかったら自動的に作成される
    db = client.knock64

    # コレクションの呼び出し、RDBでいうとテーブル、なかったら自動的に作成される
    collection = db.artist_info

    for n, value in enumerate(collection.find({'tags.value': 'dance'}).sort('rating.count', pymongo.DESCENDING), 1):
        # json.dumps(value, indent=2) はエラー
        # idが特殊な型であるから変換できない、idを削除
        del value["_id"]

        if 'rating' in value:
            rationg_count = value['rating']['count']
        else:
            rationg_count = '投票数なし'

        print(f"{n}位 {value['name']} {rationg_count}")

        if n == 10:
            break


if __name__ == '__main__':
    main()

