import pymongo


def search_artist(name):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.knock64_DB
    collection = db.collection_artists

    for result in collection.find({'name': name}):
        yield result


if __name__ == '__main__':
    for result in search_artist('Queen'):
        print(result)
