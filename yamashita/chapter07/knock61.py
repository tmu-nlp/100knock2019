import leveldb

db = leveldb.LevelDB('knock60_DB')

while True:
    a_name = input('アーティスト名を入力してください：')
    try:
        area = db.Get(a_name.encode('utf-8')).decode('utf-8')
        print(f'活動地域：{area}')
    except KeyError:
        print(f'{a_name}はDBに存在しません')
