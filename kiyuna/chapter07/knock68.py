'''
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多い
アーティスト・トップ10を求めよ．
'''
from pymongo import MongoClient as MC, DESCENDING


if __name__ == '__main__':
    c = MC('localhost', 27017).artist_db.artist_collection
    res1 = tuple(c.find({'tags.value': 'dance'}, sort=[('rating.count', DESCENDING)], limit=10))
    res2 = tuple(c.find({'tags.value': 'dance'}).sort('rating.count', DESCENDING).limit(10))
    assert res1 == res2

    for d in res1:
        print(f"{d['rating']['count']:4d}| {d['name']} ({d['id']})")
