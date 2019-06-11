# 67. 複数のドキュメントの取得
# 特定の（指定した）別名を持つアーティストを検索せよ．

from pymongo import MongoClient


def get_artist(name: str) -> list:
    client = MongoClient('localhost', 27017)

    # DBの呼び出し（なかったら作る）
    db = client['64mongo']

    # Collectionの呼び出し（なかったら作る）
    collection = db['64mongo-collection']

    return list(collection.find({'aliases.name': name}))


def main():
    name = 'The Five Saints'
    print(get_artist(name))


if __name__ == '__main__':
    main()

# 46675
