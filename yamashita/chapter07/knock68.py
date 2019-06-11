import pymongo


def search_tag_topten(tag):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.knock64_DB
    collection = db.collection_artists

    for result in collection.find({'tags.value': tag}).sort([('rating.count', -1)]).limit(10):
        yield result


if __name__ == '__main__':
    for result in search_tag_topten('dance'):
        print(result)
