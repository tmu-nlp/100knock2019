#Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．

import redis
import json
import time

db = redis.StrictRedis(host='localhost', port=6379, db=0)

def reg(db):
    db.flushall()
    path =r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter07\artist.json"
    with open(path, mode="r", encoding= "utf-8") as f:
        for line in f:
            json_line = json.loads(line)
            name = json_line.get("name") 
            id = json_line.get("id")
            area = json_line.get("area", "")
            db.hset(name, id, area)

reg(db)

print(db.dbsize())

