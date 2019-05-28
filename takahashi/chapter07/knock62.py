# 62. KVS内の反復処理
# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．

from redis import Redis
from knock60 import init


def search_artists(area=b"Japan") -> int:
    r = Redis(host="localhost", port=6379, db=0)
    return sum(1 for key in r.keys() if r.get(key) == area)


if __name__ == "__main__":
    # init()
    print(search_artists())
