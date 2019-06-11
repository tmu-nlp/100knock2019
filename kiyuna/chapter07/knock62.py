'''
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
'''
import sys
import leveldb


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


db_name = 'name2area'
db = leveldb.LevelDB(db_name)

tgt = b'Japan'
cnt = sum(1 for k, v in db.RangeIter() if v == tgt)

message(f"[+] {cnt} 件")
