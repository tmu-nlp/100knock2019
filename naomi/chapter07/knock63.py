# 63. オブジェクトを値に格納したKVS
# KVSを用い，アーティスト名（name）から
# タグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．
# さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．

import plyvel
import json
import gzip
import pickle


def save_db_tag(path: str):
    # DBの作成
    db = plyvel.DB('./db63/', create_if_missing=True)

    with gzip.open(path, 'rt', encoding='utf-8') as f:
        for line in f:
            # Jsonファイルからデータのとりだし
            artist = json.loads(line)

            if 'name' in artist and 'tags' in artist:
                # 名前がキー、場所がバリュー
                db.put(artist['name'].encode('utf-8'),
                       pickle.dumps(artist['tags']))
        db.close()


def get_tags(name: str) -> list:

    db = plyvel.DB('./db63/', create_if_missing=False)
    try:
        # Uincodeキーなので、encodeでバイト列にする
        tags = pickle.loads(db.get(name.encode('utf-8')))

    except LookupError:
        tags = 'not found'

    return tags


def main():
    path = 'artist.json.gz'
    save_db_tag(path)
    tags = get_tags('Rezerwat')
    for tag in tags:
        print(tag['count'])
        print(tag['value'])


if __name__ == '__main__':
    main()
