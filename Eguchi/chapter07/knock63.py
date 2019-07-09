#KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．
#さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
from tqdm import tqdm
import redis
import json
import time
import re

db = redis.StrictRedis(host='localhost', port=6379, db=0)

def reg(db):
    db.flushall()
    path =r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter07\artist.json"
    with open(path, mode="r", encoding= "utf-8") as f:
        for line in tqdm(f):
            json_line = json.loads(line)
            name = json_line.get("name") 
            tag_len = len(json_line.get("tags", ""))
            db.hset(name, "num", tag_len)
            if tag_len > 0:
                tag = ""
                for tagename in json_line.get("tags"):
                    tag += tagename["value"] + ", "
                db.hset(name, "content", tag)
    
    print("%d件登録" %db.dbsize())

def finder(name):
    for key, value in db.hgetall(name).items():
        if "num" in str(key):
            num = str(value)
            num = re.match("b'(\d)?'", num)

        elif "content" in str(key):
            tag = str(value)
            tag = re.match("b'(.*)'", tag)

    print("アーティスト名：%s　被タグ数：%s　タグ:%s" %(name, num.group(1), tag.group(1)))        

#reg(db)

#name = input("アーティスト名を入力---->")
name = "Taylor Swift"
finder(name)