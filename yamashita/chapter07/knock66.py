import pymongo


def count_by_area(area):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.knock64_DB
    collection = db.collection_artists

    c = collection.count({'area': area})
    return c


if __name__ == '__main__':
    print(count_by_area('Japan'))
