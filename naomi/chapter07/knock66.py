# 66. 検索件数の取得
# MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．


from pymongo import MongoClient


def get_artistcounts(area: str) -> int:
    client = MongoClient('localhost', 27017)

    # DBの呼び出し（なかったら作る）
    db = client['64mongo']

    # Collectionの呼び出し（なかったら作る）
    collection = db['64mongo-collection']

    return collection.find({'area': area}).count()


def main():
    area = 'Japan'
    print(get_artistcounts(area))
 

if __name__ == '__main__':
    main()

# 46675
