# 60. KVSの構築
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を
# 検索するためのデータベースを構築せよ．

import plyvel
import json
import gzip


def save_db(path: str):
    # DBの作成
    db = plyvel.DB('./db/', create_if_missing=True)
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        for line in f:
            # Jsonファイルからデータのとりだし
            artist = json.loads(line)
            if 'name' in artist and 'area' in artist:
                # 名前がキー、場所がバリュー
                db.put(artist['name'].encode('utf-8'),
                       artist['area'].encode('utf-8'))
        db.close()


def main():
    path = 'artist.json.gz'
    save_db(path)


if __name__ == '__main__':
    main()
