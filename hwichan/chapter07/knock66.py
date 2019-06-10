import pymongo
from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)  # 第一引数にはアドレス、第二引数にはポート番号

    # データベースの呼び出し、なかったら自動的に作成される
    db = client.knock64

    # コレクションの呼び出し、RDBでいうとテーブル、なかったら自動的に作成される
    collection = db.artist_info

    print(collection.count({'area': 'Japan'}))

    # インタラクティブシェル  db.artist_info.count({area : 'Japan'})


if __name__ == '__main__':
    main()

