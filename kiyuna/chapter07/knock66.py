'''
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，
活動場所が「Japan」となっているアーティスト数を求めよ．
'''
from pymongo import MongoClient as MC


if __name__ == '__main__':
    collection = MC('mongodb://localhost:27017/').artist_db.artist_collection
    res = sum(1 for _ in collection.find({'area': "Japan"}))
    print(res)


'''
* MongoDB のインタラクティブシェルを用いて，
  活動場所が「Japan」となっているアーティスト数を求める
    - show dbs
    - use artist_db
    - show collections
    - db.artist_collection.find({'area': 'Japan'}).count()
'''
