# 60. KVSの構築
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を
# 検索するためのデータベースを構築せよ．

from redis import Redis
import gzip
import json


def init():
    r = Redis(host="localhost", port=6379, db=0)
    pipe = r.pipeline()
    # rt : テキストで読み出す (r : バイナリで読み込む)
    for i, line in enumerate(
        gzip.open("../data/artist.json.gz", "rt", encoding="utf-8"), 1
    ):
        artist = json.loads(line)
        if "name" in artist and "area" in artist:
            name, area = artist["name"], artist["area"]
            pipe.set(name, area)
        # 10k ごとにパイプライン処理を実行する
        if i % 10000 == 0:
            pipe.execute()
    pipe.execute()
    print(f"stored {len(r.keys())} items ")


if __name__ == "__main__":
    init()
