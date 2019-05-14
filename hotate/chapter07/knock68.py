from knock64 import ArtistDB


if __name__ == '__main__':
    db = ArtistDB()
    for rank in db.collection.find({"tags.value": "dance"}).sort([("rating.count", -1)]).limit(10):
        print(f'{rank["name"]}\t{rank["rating"]["count"]}')
