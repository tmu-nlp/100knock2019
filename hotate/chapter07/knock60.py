import json
import plyvel


def main():
    db = plyvel.DB('./db_knock60/', create_if_missing=True)
    for line in open('artist.json', 'r'):
        artist_dic = json.loads(line)
        if {'name', 'area'}.issubset(set(artist_dic.keys())):
            db.put(artist_dic['name'].encode('utf-8'), artist_dic['area'].encode('utf-8'))
    db.close()


if __name__ == '__main__':
    main()
