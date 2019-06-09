# 60. KVSの構築
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．

import plyvel
import json
import gzip

db = plyvel.DB('./db', create_if_missing=True)

with gzip.open('artist.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        d_artist = json.loads(line)
        if 'name' and 'area' in d_artist:
            db.put(d_artist['name'].encode('utf-8'),
                   d_artist['area'].encode('utf-8'))
    db.close()
