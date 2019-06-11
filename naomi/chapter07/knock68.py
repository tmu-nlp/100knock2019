# 68. ソート
# "dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．

from pymongo import MongoClient


def get_artist(tag: str) -> list:
    client = MongoClient()

    # DBの呼び
    # 出し（なかったら作る）
    db = client['64mongo']

    # Collectionの呼び出し（なかったら作る）
    collection = db['64mongo-collection']

    for artist in (collection.find({'tags.value': tag}).
                   sort([('rating.count', -1)]).limit(10)):
        yield f"{artist['name']}: {artist['rating']['count']}"


def main():
    tag = 'dance'
    for info in get_artist(tag):
        print(info)


if __name__ == '__main__':
    main()

# 46675
