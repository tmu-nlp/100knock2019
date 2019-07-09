#60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．

import redis

def finder(artistname):
    db = redis.StrictRedis(host='localhost', port=6379, db=0)
    area = db.hgetall(artistname)
    return area

artistname = input('アーティスト名を入力してください--> ')
area = finder(artistname)

print(area.values())

