import leveldb
import gzip
import json

db = leveldb.LevelDB('knock60_DB')
with gzip.open('artist.json.gz', 'rt', encoding='utf-8') as i_file:
    for line in i_file:
        artist = json.loads(line)
        if not('name' in artist) or not('area' in artist):
            continue
        db.Put(artist['name'].encode('utf-8'), artist['area'].encode('utf-8'))
