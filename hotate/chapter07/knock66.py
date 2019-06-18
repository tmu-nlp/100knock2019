#  db.artist.find({"area":"Japan"}).count()
from knock64 import ArtistDB


def main():
    db = ArtistDB()
    print(db.collection.find({"area": "Japan"}).count())


if __name__ == '__main__':
    main()
