import pymongo


def search_by_alias(alias):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.knock64_DB
    collection = db.collection_artists

    for result in collection.find({'aliases.name': alias}):
        yield result


if __name__ == '__main__':
    s = input('検索したい別名を入力してください：')
    for result in search_by_alias(s):
        print(result)
