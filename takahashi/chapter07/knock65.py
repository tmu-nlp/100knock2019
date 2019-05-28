# 65. MongoDBの検索
# MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
# さらに，これと同様の処理を行うプログラムを実装せよ．

from pymongo import MongoClient


def search_artist(name: str) -> list:
    client = MongoClient("localhost", 27017)
    db = client.nlp100_knock
    col = db.artists

    results = []
    for x in col.find({"name": name}):
        results.append(x)

    return results


if __name__ == "__main__":
    for i in search_artist("Queen"):
        print(i)
