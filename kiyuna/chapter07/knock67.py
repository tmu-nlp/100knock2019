'''
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ．
'''
from pymongo import MongoClient as MC


if __name__ == '__main__':
    collection = MC('localhost', 27017).artist_db.artist_collection
    for d in collection.find({'aliases.name': 'Evaldas Azbukauskas'}):
        print(d)


'''
* 共通の aliases.name を持っているのは何種類あるか
    - 2 種類 -> 224 つ
    - 3 種類 -> 8 つ
        'LSD', 'Nicole', 'Jerry', 'Pete Abbott',
        'Stephen Baxter', 'Max', 'Jessica', 'Johnny'
    - 4 種類 -> 1 つ
        'Evaldas Azbukauskas'
'''
