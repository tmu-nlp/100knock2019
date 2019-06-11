'''
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
'''
import sys
import leveldb


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


db_name = 'name2area'
db = leveldb.LevelDB(db_name)

message("[*] key = Oasis*")
for key, value in db.RangeIter(key_from=b'Oasis'):
    name, id = key.decode().split('\t')
    area = value.decode()
    if 'Oasis' not in name:
        break
    print(f'{name} (id={id}) -> {area}')

message("[*] key = Oasis\t20660")
print(db.Get(b'Oasis\t20660').decode())


'''
* 参考
- https://qiita.com/segavvy/items/41b860ca0d0c7d8facc9
'''
