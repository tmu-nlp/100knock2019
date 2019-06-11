'''
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
さらに，これと同様の処理を行うプログラムを実装せよ．
'''
import json
from pymongo import MongoClient
from bson.objectid import ObjectId


def support_ObjectId(obj):
    ''' json.dumps() で ObjectId を処理するためのコールバック関数
    ObjectId は json エンコードできない型なので、文字列型に変換する

    https://qiita.com/segavvy/items/d360c2568b49bd5c153a
    https://qiita.com/podhmo/items/dc748a9d40026c28556d
    '''
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(repr(obj) + " is not JSON serializable")


if __name__ == '__main__':
    db_name = 'artist_db'
    collection_name = 'artist_collection'

    collection = MongoClient('localhost', 27017)[db_name][collection_name]

    for d in collection.find({'name': "Queen"}):
        print(json.dumps(d, indent='  ', sort_keys=True, default=support_ObjectId))


'''
* MongoDB のインタラクティブシェルを用いて，"Queen" というアーティストに関する情報を取得
    - show dbs
    - use artist_db
    - show collections
    - db.artist_collection.find({'name': 'Queen'})

* json.dump
    - https://docs.python.org/ja/3/library/json.html#json.dump
'''
