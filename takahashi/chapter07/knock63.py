# 63. オブジェクトを値に格納したKVS
# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）の
# リストを検索するためのデータベースを構築せよ．
# さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．

from redis import Redis
import gzip
import json


def init():
    r = Redis(host="localhost", port=6379, db=0)
    pipe = r.pipeline()
    count = 1
    for line in gzip.open("../data/artist.json.gz", "rt", encoding="utf-8"):
        artist = json.loads(line)
        if "name" in artist and "tags" in artist:
            pipe.set(artist["name"], json.dumps(artist["tags"]))
            count += 1

        if count % 1000 == 0:
            pipe.execute()
    pipe.execute()
    print(f"stored {count-1} items")


def search_tags(name: str) -> dict:
    r = Redis(host="localhost", port=6379, db=0)
    item = r.get(name)
    if item:
        return json.loads(item)
    else:
        return None


if __name__ == "__main__":
    # init()
    artist = input("artist name: ").rstrip()
    result = search_tags(artist)
    if result:
        for r in result:
            print(f"{r['value']}\t({r['count']})")
