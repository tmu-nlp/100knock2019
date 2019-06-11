# 65. MongoDBの検索
# MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
# さらに，これと同様の処理を行うプログラムを実装せよ．
from pymongo import MongoClient


def get_artists(name: str) -> list:
    client = MongoClient('localhost', 27017)

    # DBの呼び出し（なかったら作る）
    db = client['64mongo']

    # Collectionの呼び出し（なかったら作る）
    collection = db['64mongo-collection']

    return list(collection.find({'name': name}))


def main():
    name = 'Queen'
    artists = get_artists(name)
    for artist in artists:
        print(artist)


if __name__ == '__main__':
    main()
