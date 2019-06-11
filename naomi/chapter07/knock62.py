# 62. KVS内の反復処理
# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
import plyvel


def get_artistcounts(name: str) -> int:

    db = plyvel.DB('./db', create_if_missing=False)

    counts = 0
    for key, value in db:
        if value == name.encode('utf-8'):
            counts += 1
            print(key.decode())
    db.close()
    return counts


def main():
    area = 'Japan'
    counts = get_artistcounts(area)
    print(counts)


if __name__ == '__main__':
    main()
