import leveldb
import gzip
import json


def make_db():
    try:
        db = leveldb.LevelDB('knock63_DB', error_if_exist=True)
        with gzip.open('artist.json.gz', 'rt', encoding='utf-8') as i_file:
            for line in i_file:
                artist = json.loads(line)
                if 'name' not in artist or 'tags' not in artist:
                    continue
                db.Put(artist['name'].encode('utf-8'),
                       json.dumps(artist['tags']).encode('utf-8'))
    except:
        db = leveldb.LevelDB('knock63_DB')


def search_tags(name):
    db = leveldb.LevelDB('knock63_DB')
    try:
        return json.loads(db.Get(name.encode('utf-8')))
    except:
        return None


if __name__ == '__main__':
    make_db()
    while True:
        name = input('アーティスト名を入力してください：')
        tags = search_tags(name)
        if tags:
            for tag in tags:
                print(f'{tag["value"]} : {tag["count"]}')
        else:
            print(f'{name}はDBに存在しません')
