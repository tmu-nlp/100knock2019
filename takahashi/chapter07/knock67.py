# 67. 複数のドキュメントの取得
# 特定の（指定した）別名を持つアーティストを検索せよ．

from pymongo import MongoClient


def search_artist(name: str) -> list:
    client = MongoClient("localhost", 27017)
    db = client.nlp100_knock
    col = db.artists

    results = []
    for x in col.find({"aliases.name": name}):
        results.append(x)

    return results


if __name__ == "__main__":
    for i in search_artist("Queen"):
        print(i)
