'''
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
'''


import leveldb
import sys
import re


def Get_area(db_path, artist_name):
    db = leveldb.LevelDB(db_path)
    # reg = re.compile(r"(?<=bytearray\(b')\S+(?='\))")
    # str_ = str(db.Get(artist_name.encode()))
    # area = reg.search(str_)
    # print(area.group(0))
    # if artist_name.encode() in db:
    print(db.Get(artist_name.encode()).decode())


if __name__ == "__main__":
    db_path = "lvdb"
    Get_area(db_path, " ".join(sys.argv[1:]))
