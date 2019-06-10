import leveldb


def main():
    db = leveldb.LevelDB('knock60')
    search_name = input('アーテイスト名 : ')

    # RangeIter() dbの要素をイテレーターで取得
    for name, area in db.RangeIter():
        # bytes.decode()でバイト列から文字列に変換
        name = name.decode().split('_')[0]
        if name == search_name:
            print(name, area.decode())


if __name__ == '__main__':
    main()

