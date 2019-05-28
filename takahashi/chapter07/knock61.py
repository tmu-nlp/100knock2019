# 61. KVSの検索
# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．

from redis import Redis
from knock60 import init


def search_area_by_name(name: str) -> str:
    r = Redis(host="localhost", port=6379, db=0)
    return r.get(name)


if __name__ == "__main__":
    # init()
    artist = input("artist name: ").rstrip()
    print(search_area_by_name(artist))
