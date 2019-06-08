'''
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を\
    検索するためのデータベースを構築せよ．
'''


import leveldb
import json


def built_KVS(path):
    with open(path, "r") as f:
        count = 0
        db = leveldb.LevelDB('./lvdb')
        for line in f:
            jsonData = json.loads(line)
            if "name" in jsonData and "area" in jsonData:
                db.Put(jsonData["name"].encode(), jsonData["area"].encode())


if __name__ == "__main__":
    path = "artist.json"
    built_KVS(path)
