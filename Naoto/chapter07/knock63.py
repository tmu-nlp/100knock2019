'''
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．\
    さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
'''


import leveldb
import json
import sys


def KVS_build_tags(json_path, db_path):
    db = leveldb.LevelDB(db_path)
    with open(json_path) as f:
        for line in f:
            json_Data = json.loads(line)
            tag_list = []
            if "tags" in json_Data:
                for i, tag in enumerate(json_Data["tags"]):
                    tag_list.append(tag["value"])
                tag_list.insert(0, str(i+1))
                db.Put(json_Data["name"].encode(), "^".join(tag_list).encode())
                # listをjoinさせて文字列として格納しておくことで、後でdecodeしてからsplitでlist型へ戻せる。
                # スペースでjoinすると、タグ名がスペースの場合、区切られてしまう


def KVS_tags_find(db_path, artist):
    db = leveldb.LevelDB(db_path)
    print(db.Get(artist.encode()).decode().split("^"))


if __name__ == "__main__":
    json_path = "artist.json"
    db_path = "KVS_tags"
    if sys.argv[1] == "build":
        KVS_build_tags(json_path, db_path)
        KVS_tags_find(db_path, " ".join(sys.argv[2:]))
    else:
        KVS_tags_find(db_path, " ".join(sys.argv[1:]))
