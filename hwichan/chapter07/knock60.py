import gzip
import json
import leveldb


def main():
    db = leveldb.LevelDB('knock60')  # dbを指定、なかったら自動で作成
    with gzip.open('artist.json.gz', "rt", "utf_8") as f:
        for line in f:
            json_data = json.loads(line)  # jsonデータを辞書型に変換
            name = f"{json_data['name']}_{json_data['id']}"  # nameが同じ場合があるためidを付ける
            if 'area' in json_data:
                area = json_data['area']
            else:
                area = ''

            # str.encode()で文字列からバイト列に変換
            db.Put(name.encode(), area.encode())


if __name__ == '__main__':
    main()

