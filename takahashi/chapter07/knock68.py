# 68. ソート
# "dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．

from pymongo import MongoClient, DESCENDING


def search_high_rating_in_dance() -> list:
    client = MongoClient("localhost", 27017)
    db = client.nlp100_knock
    col = db.artists

    return list(
        col.find({"tags.value": "dance"}).sort("rating.count", DESCENDING).limit(10)
    )


if __name__ == "__main__":
    for artist in search_high_rating_in_dance():
        print(f"{artist['name']} ({artist['rating']['count']})")
