'''
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．
'''


'''
> db.artist_collection.find({area:'Japan'}).count()
45642
'''
