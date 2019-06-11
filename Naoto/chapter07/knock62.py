'''
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
'''


import leveldb


def Japan_artists_num(db_path) -> int:
    db = leveldb.LevelDB(db_path)
    num = 0
    for k, v in db.RangeIter():
        if v == "Japan".encode():
            num += 1
    return num


if __name__ == "__main__":
    db_path = "KVS_area"
    num = Japan_artists_num(db_path)
    print(num)
