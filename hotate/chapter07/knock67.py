import json

from knock64 import ArtistDB


def main():
    db = ArtistDB()
    while True:
        aliases_name = input('Please enter an alias name. (quit command: "q")\n')
        if aliases_name == 'q':
            break
        else:
            info_list = list(db.search_aliases(aliases_name))
            if len(info_list) != 0:
                for info in info_list:
                    del info['_id']
                    print(json.dumps(info, indent=2))
            else:
                print('The alias name is not registered.')
            print('-' * 100)


if __name__ == '__main__':
    main()

# mongo
# use knock64
# db.artist.find({"aliases.name":"Queen"})
