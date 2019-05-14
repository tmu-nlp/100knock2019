#  db.artist.find({"area":"Japan"}).count()
from knock64 import ArtistDB


if __name__ == '__main__':
    db = ArtistDB()
    print(db.collection.find({"area": "Japan"}).count())
