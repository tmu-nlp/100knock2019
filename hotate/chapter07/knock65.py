from knock64 import ArtistDB
import json


if __name__ == '__main__':
    db = ArtistDB()
    while True:
        artist_name = input('Please enter an artist name. (quit command: "q")\n')
        if artist_name == 'q':
            break
        else:
            info_list = list(db.artist_info(artist_name))
            if len(info_list) != 0:
                for info in info_list:
                    del info['_id']
                    print(json.dumps(info, indent=2))
            else:
                print('The artist name is not registered.')
            print('-'*100)


# mongo
# use knock64
# db.artist.find({"name":"Queen"})
