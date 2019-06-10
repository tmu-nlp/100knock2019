import gzip
import json
import leveldb


def create_db():
    db = leveldb.LevelDB('knock60_tag')
    with gzip.open('artist.json.gz', "rt", "utf_8") as f:
        for line in f:
            json_data = json.loads(line)  # jsonデータを辞書型に変換
            name = f"{json_data['name']}_{json_data['id']}"
            tags = json_data.get('tags', [])  # json_dataにtagsがあったらそのまま、なかったら[]を指定

            # json.dumps : list dictなどをjson形式にエンコード
            # https://www.sejuku.net/blog/79338
            db.Put(name.encode(), json.dumps(tags).encode())


def main():
    # dbの作成
    # create_db()

    db = leveldb.LevelDB('knock60_tag')
    search_name = input('アーテイスト名 : ')

    for name, tags in db.RangeIter():
        name, name_id = name.decode().split('_')[0], name.decode().split('_')[1]
        if name == search_name:
            print(f'{name}(id={name_id})')
            tags = json.loads(tags)
            if len(tags) > 0:
                for tag in tags:
                    print(f"タグ : {tag['value']}, 被タグ数 : {tag['count']}")
            else:
                print('タグはありません')


if __name__ == '__main__':
    main()

