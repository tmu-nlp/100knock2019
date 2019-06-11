# 61. KVSの検索
# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．

import plyvel


def get_area(name: str) -> str:

    db = plyvel.DB('./db', create_if_missing=False)

    try:
        # Uincodeキーなので、encodeでバイト列にする
        area = db.get(name.encode('utf-8'))

        # バイト列を文字列にする
        # b'United States' -> United States
        area = area.decode()

    except LookupError:
        area = 'not found'

    db.close()
    return area


def main():
    artist = 'The Blackbelt Band'
    artist = 'The Wanderers'
    artist = 'Gülten Kaya Hayaloğlu'
    area = get_area(artist)
    print(area)


if __name__ == '__main__':
    main()

# The Wanderers: United States